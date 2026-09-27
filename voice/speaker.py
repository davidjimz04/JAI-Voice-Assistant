import pyttsx3
import re

def speak(text):
    engine = pyttsx3.init()

    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[114].id)
    engine.setProperty('rate', 185)
    engine.setProperty('volume', 0.7)

    separated_text = re.split(r'(?<=[.!?])\s+', text)
    for part in separated_text:
        part = part.strip()

        if part:
            engine.say(part)
    engine.runAndWait()