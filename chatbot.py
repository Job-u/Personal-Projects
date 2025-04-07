import openai
import speech_recognition as sr
from gtts import gTTS
import os
import time

# Set your OpenAI API key
openai.api_key = "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"

# Function to get AI response
def get_response(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",  # You can change to gpt-4 if you have access
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content.strip()

# Function to convert text to speech
def speak(text, lang='en'):
    tts = gTTS(text=text, lang=lang)
    filename = "output.mp3"
    tts.save(filename)
    os.system("start " + filename)  # Windows; use "afplay" on Mac or "mpg123" on Linux

# Function to recognize speech
def listen():
    recognizer = sr.Recognizer()
    mic = sr.Microphone()

    with mic as source:
        print("🎙️ Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        print("🧠 Recognizing...")
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return "Sorry, I didn't catch that."
    except sr.RequestError:
        return "Could not request results."

# Main loop
print("🗣️ AI Voice Chatbot Ready. Say 'quit' to exit.")
while True:
    user_input = listen()
    print("You:", user_input)

    if user_input.lower() == "quit":
        break

    response = get_response(user_input)
    print("Chatbot:", response)
    speak(response)
