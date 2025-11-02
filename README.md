🎓 Flash AI — Interactive Educational Assistant

An AI-powered learning companion that can understand user queries via text or voice, and respond with clear, structured explanations across academic subjects — from Mathematics and Computer Science to Geography and General Knowledge.

🧠 Overview

Flash AI is designed to make learning interactive, accessible, and engaging.
It allows users to:

Ask questions in text or voice format.

Receive responses in text and audio.

View animated, learner-friendly interactions in the frontend.

Understand academic or technical concepts explained in a clear, structured manner.

This project demonstrates how Generative AI, speech recognition, and frontend interactivity can combine to build a smart, educational assistant.

✨ Key Features

🎤 Dual Mode Interaction — Users can choose between Text Mode or Voice Mode.

🗣️ AI Speaks Back — The assistant speaks the response aloud for auditory learners.

🧩 Educationally Tuned UI — The interface feels friendly, academic, and interactive.

🔍 Knowledge Integration — The assistant can analyze images or text inputs (future upgrade).

🪄 Real-Time Thinking Animations — Smooth, learner-friendly effects make the experience engaging.

🧰 Tech Stack
Layer	Technology
Frontend	HTML, CSS, JavaScript
Backend	Python (Flask)
AI Model	Google Gemini / Gemini 1.5 Pro
APIs / Libraries	google-generativeai, speech_recognition, pyttsx3, requests
Design	Animated, modern learner interface (educational theme)
🚀 Getting Started
1️⃣ Clone this Repository
git clone https://github.com/your-username/flash-ai-assistant.git
cd flash-ai-assistant

2️⃣ Install Dependencies
pip install -r requirements.txt

3️⃣ Add Your API Key

Create a .env file or edit main.py to include your Google Gemini API key:

genai.configure(api_key="YOUR_API_KEY_HERE")

4️⃣ Run the Flask Server
python main.py

5️⃣ Open in Browser

Navigate to:
👉 http://127.0.0.1:5000/

You’ll see the educational interface of Flash AI, ready to chat.

🧩 How It Works

Frontend (index.html)

Displays the interactive chatbot UI.

Lets users enter text or use voice via the mic button.

Animations enhance engagement.

Backend (main.py)

Handles API requests and user input.

Processes text or audio queries.

Sends the response to the frontend and speaks it aloud.

CSS (style.css)

Theming focused on educational clarity: soft gradients, glowing highlights, and readable fonts.

🧭 Future Enhancements

🖼️ Image Understanding — Upload diagrams or equations for AI-based analysis.

🎬 Video Output — AI-generated short video explanations for complex topics.

🗂️ Topic History — Track previous learning sessions.

📊 Graphical Answers — Math plots and conceptual infographics.

📚 Educational Use Cases

✳️ Maths Tutor – Explain formulas and derivations step by step.

💻 CS Assistant – Clarify programming concepts or algorithms.

🌍 Geography Aid – Visualize and describe locations, processes, and maps.

🔬 Science Explainer – Simplify physics or biology concepts interactively.

🤝 Contributors
Name	Role	Description
Bhaskar Anand:	Lead Developer	Built the full-stack integration, UI, and AI pipeline.
Arnav Khare, Somnath Gorai, Basab Priyo Biswas, Himesh:	AI / Backend / Frontend	Developed the educational UX and backend logic.
Presented by Arnav Khare


💬 Acknowledgements

Google Generative AI API
 for Gemini models.

SpeechRecognition
 for voice input.

Pyttsx3
 for text-to-speech output.

🌟 Inspiration

“Learning should not be limited by medium — Flash AI brings knowledge closer to every learner, whether they read, listen, or explore visually.”
