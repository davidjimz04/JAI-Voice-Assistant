import speech_recognition as sr
from voice.speaker import speak

def listen() -> str:
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