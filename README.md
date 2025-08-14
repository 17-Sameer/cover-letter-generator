Created this AI Cover Letter Generator as a first AI and HTML project, to learn and get experience with AI. User inputs The Job title and Company, as well as a short resume summary, then they can generate the cover letter.

Using Python as backend :

Flask → to run the web server and handle requests (from flask import Flask, request, jsonify, render_template)

transformers → to load and run the Qwen language model (AutoTokenizer, AutoModelForCausalLM)

torch → backend framework used by the Transformers model for inference

Used HTML and CSS as frontend and Vanilla JavaScript for API calls.

Limitations: This AI Qwen-3 is a small model with only 600M parameters, and it was untrained, will be looking to use bigger models as well as training for my next AI project.
I chose this AI as it was free and lightweight enough for my laptop to host locally.
This AI has some common errors generating cover letters, it spits out some weird brackets and has weird text document formatting thrown in at the beginning. Then it finds its footing and begins writing properly with some small errors. 
Will learn more about prompt engineering next time to avoid this result.
