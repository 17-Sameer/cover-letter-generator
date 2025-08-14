from flask import Flask, request, jsonify, render_template
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

app = Flask(__name__)

MODEL_NAME = "Qwen/Qwen3-0.6B"
print("Loading model and tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)
print(f"Model loaded on {device}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_cover_letter():
    data = request.json
    job_title = data.get("jobTitle", "").strip()
    company = data.get("company", "").strip()
    resume_summary = data.get("resumeSummary", "").strip()

    if not job_title or not company or not resume_summary:
        return jsonify({"error": "Please provide jobTitle, company, and resumeSummary"}), 400

    prompt = (
        f"Write a professional cover letter applying for the position of {job_title} at {company}.\n\n"
        f"Do not repeat statements "
        f"Do not include any non alphabet characters"
        f"Do not repeat the prompt"
        f"The letter should sound natural and engaging, highlighting the candidate's passion "
        f"relevant skills, and how they can contribute to the team. Use a formal, professional tone and include a polite closing.\n\n"
        f"Start with \"Dear Hiring Manager,\""
    )

    try:
        inputs = tokenizer(prompt, return_tensors="pt").to(device)
        outputs = model.generate(
            **inputs,
            max_length=300,
            do_sample=True,
            temperature=0.7,
            top_p=0.9,
            eos_token_id=tokenizer.eos_token_id,
            pad_token_id=tokenizer.pad_token_id,
        )
        generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Trim prompt from output if repeated
        if generated_text.startswith(prompt):
            generated_text = generated_text[len(prompt):].strip()

        return jsonify({"coverLetter": generated_text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500



if __name__ == '__main__':
    app.run(debug=True, port=5000)
