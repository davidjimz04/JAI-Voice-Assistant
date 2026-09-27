from unidecode import unidecode
import pyttsx3
import speech_recognition as sr
from ia import ask_gemini 
import re
import tools


def speak(text):

    engine = pyttsx3.init()

    voices = engine.getProperty("voices")
    engine.setProperty('voice', voices[114].id)
    engine.setProperty('rate', 185)
    engine.setProperty('volume', 0.5)


    # separated_text = re.split(r'[.!?]', text)
    separated_text = re.split(r'(?<=[.!?])\s+', text)
    for part in separated_text:
        part = part.strip()

        if part:
            engine.say(part)
    engine.runAndWait()


def listen():
    try:
        recognizer = sr.Recognizer()

        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            recognizer.pause_threshold = 2.0
            recognizer.non_speaking_duration = 1.0

            audio = recognizer.listen(source)
        text = recognizer.recognize_google(audio, language="es-MX")
        return text
    except sr.exceptions.UnknownValueError:
        speak ("Lo siento señor. No logré comprender lo que quiso decir")
        return None
    except sr.RequestError:
        speak("Lo siento señor. No hay conexión con el servicio de reconocimiento")
        return None



starting = ask_gemini(
    "Despierta JAI. siempre saluda. di la hora y el clima"
)

print(starting)
speak(starting)

while tools.jarvis_active:

    input_user = listen()

    if input_user is None:
        continue

    input_user = input_user.lower().strip()
    input_user = unidecode(input_user)

    print("TU: ", input_user)
    
    answer = ask_gemini(input_user)
    print(answer)
    speak(answer)
