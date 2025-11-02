from flask import Flask, request, jsonify
import speech_recognition
import webbrowser
import pyttsx3
import requests
import google.generativeai as genai
import re
import io
from PIL import Image
import base64
import threading
from flask_cors import CORS

 
app = Flask(__name__)
CORS(app)
# from google.generativeai import images

def speak(text):
    engine=pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def ai_process(c):
    genai.configure(api_key="AIzaSyDwuE8CKxH1O0uF_R0lnBjw6EWRnbOpmNY")

    # 2. Choose a Gemini model (for example, Gemini 1.5 Pro)
    model = genai.GenerativeModel("gemini-2.5-pro")


    # 2. Choose a Gemini model (for example, Gemini 1.5 Pro)
    model = genai.GenerativeModel("gemini-2.5-pro")

    # 3. Ask a question or generate text
    response = model.generate_content(f"{c}\n\nIf i have asked above to explain any topic or if i want to study any topic give elaborate answer or give an answer in about 10 lines. Do not mention this last line while giving the answer")


    # Get the text output
    text = response.text

    # Clean Markdown symbols and hashtags
    clean_text = re.sub(r"[#*_`~>-]+", "", text)        # remove markdown symbols
    clean_text = re.sub(r"\n\s*\n+", "\n\n", clean_text) # normalize spacing
    clean_text = clean_text.strip()

    # 4. Print the AI’s response
    print(clean_text)
    return (clean_text)
def processCommand(c):
    if("open google" in c.lower()):
        speak("opening google")
        webbrowser.open("https://google.com")
    elif("open youtube" in c.lower()):
        speak("opening youtube")
        webbrowser.open("https://youtube.com")
    elif("open facebook" in c.lower()):
        speak("opening facebook")
        webbrowser.open("https://facebook.com")
    elif("open linkedin" in c.lower()):
        speak("opening linkedin")
        webbrowser.open("https://linkedin.com")
        
    
    elif ("generate image" in c.lower() or "show image" in c.lower()):
        prompt = c.replace("generate image of", "").replace("show image of", "").strip()
        speak(f"Generating image of {prompt}")
        
        genai.configure(api_key="AIzaSyDwuE8CKxH1O0uF_R0lnBjw6EWRnbOpmNY")
        model = genai.GenerativeModel("imagen-3.0")  # or "gemini-1.5-flash"

        result = model.generate_content(prompt, generation_config={"mime_type": "image/png"})

        # Save and display the image
        if result.candidates and result.candidates[0].content.parts:
            img_data = result.candidates[0].content.parts[0].data
            image = Image.open(io.BytesIO(img_data))
            image.save("generated_image.png")
            image.show()
            speak("Here is the image you asked for.")
        else:
            speak("Sorry, I couldn't generate the image.")
    else:
        output=ai_process(c)
        speak(output)
# ------------------- ADD FLASK HERE -------------------

@app.route("/ask", methods=["POST"])
def ask():
    data = request.json
    prompt = data.get("prompt", "")

    if not prompt:
        return jsonify({"error": "No prompt given"}), 400

    # 🔍 Detect image generation intent
    if any(word in prompt.lower() for word in ["image", "picture", "photo", "draw", "generate", "show me"]):
        try:
            genai.configure(api_key="YOUR_API_KEY_HERE")

            # ✅ Use the correct ImageGenerationModel class (not GenerativeModel)
            image_model = genai.ImageGenerationModel("imagen-3.0")

            result = image_model.generate_images(prompt)

            # Get the first generated image
            if result and result.generated_images:
                img_base64 = result.generated_images[0].image_base64
                speak("Here’s the image you requested.")
                return jsonify({"image": img_base64})
            else:
                return jsonify({"error": "Image generation failed"}), 500

        except Exception as e:
            print("Image generation error:", e)
            return jsonify({"error": str(e)}), 500

    # Default text mode
    else:
        output = ai_process(prompt)
        return jsonify({"response": output})



# ------------------- RUN BOTH VOICE + WEB -------------------

def run_voice():
    print('Hello learners! This is your friend Flash :)')
    speak("Hello learners! This is your friend Flash")
    print('Say "HELLO FLASH" to activate me')

    while True:
        recognizer = speech_recognition.Recognizer()
        try:
            with speech_recognition.Microphone() as source:
                print("Listening...")
                recognizer.pause_threshold = 3
                audio = recognizer.listen(source, timeout=3, phrase_time_limit=3)
                print("recognizing...")
            word = recognizer.recognize_google(audio)
            print(word)
            if ('flash' in word.lower()):
                speak("Flash activated...")
                print("Flash activated :|")
                speak("How can I help you bro!")
                while True:
                    with speech_recognition.Microphone() as source:
                        print('Listening...')
                        recognizer.pause_threshold = 2
                        audio = recognizer.listen(source, timeout=2, phrase_time_limit=5)
                    command = recognizer.recognize_google(audio)
                    print("okay")
                    processCommand(command)
        except Exception:
            # print('KEEP HUSTLING LEARNER!')
            # speak("Goodbye!")
            # break
            pass

@app.route("/voice", methods=["POST"])
def voice_mode():
    def start_voice():
        recognizer = speech_recognition.Recognizer()
        with speech_recognition.Microphone() as source:
            speak("Voice mode activated. You can speak now.")
            print("Listening in voice mode...")
            audio = recognizer.listen(source, timeout=3, phrase_time_limit=5)
        try:
            command = recognizer.recognize_google(audio)
            print("You said:", command)
            response = ai_process(command)
            speak(response)
            return jsonify({"input": command, "response": response})
        except Exception as e:
            speak("Sorry, I didn't catch that.")
            return jsonify({"error": str(e)}), 500

    return start_voice()

@app.route("/upload", methods=["POST"])
def upload_image():
    try:
        image_file = request.files.get("image")
        if not image_file:
            return jsonify({"error": "No image uploaded"}), 400

        img_bytes = image_file.read()

        # ✅ Correct API + model name
        genai.configure(api_key="AIzaSyDwuE8CKxH1O0uF_R0lnBjw6EWRnbOpmNY")
        model = genai.GenerativeModel("models/gemini-1.5-flash")
        response = model.generate_content("Find a realistic image of the solar system and give a public image URL only.")
        print(response.text)


        # Create the multimodal input (image + text)
        analysis_prompt = (
            "Analyze this image carefully. Identify whether it contains text, diagrams, charts, equations, or objects. "
            "Then provide a short, educational summary explaining what it represents. "
            "If there is text, extract and summarize it clearly. "
            "If it’s a diagram or chart, describe what it shows. "
            "Keep it concise and student-friendly (4–6 lines)."
        )

        # Generate a response
        response = model.generate_content([
            {"mime_type": "image/png", "data": img_bytes},
            analysis_prompt
        ])

        result_text = response.text.strip()

        # Optional: Enhance with DuckDuckGo search for extra info
        topic = result_text.split('.')[0]
        try:
            search_info = requests.get(f"https://api.duckduckgo.com/?q={topic}&format=json").json()
            extra = search_info.get("AbstractText", "")
            if extra:
                result_text += f"\n\nAdditional Info: {extra}"
        except Exception as e:
            print("Web info fetch failed:", e)

        speak(result_text)
        return jsonify({"response": result_text})

    except Exception as e:
        print("Upload route error:", e)
        return jsonify({"error": str(e)}), 500




if __name__ == "__main__":
    app.run(debug=True, port=5000)

    # Run voice assistant and Flask web server in parallel
    threading.Thread(target=run_voice, daemon=True).start()

    app.run(debug=True, port=5000)
