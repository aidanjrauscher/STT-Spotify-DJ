import speech_recognition as sr

from dotenv import load_dotenv
import os
load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

def listen():
    r = sr.Recognizer()
    r.energy_threshold = 1000
    with sr.Microphone() as source:
        print('Calibrating...')

        r.adjust_for_ambient_noise(source, duration=3)
        
        print('Listening...')
        try:
            audio = r.listen(source, timeout=None)
            print('Recognizing...')
            text = r.recognize_google(audio)
            return text
        except Exception as e:
            print("No audio recorded. Make sure default microphone is working.")
            return None
    
