from unidecode import unidecode
import tools
from voice.speaker import speak
from voice.listener import listen
from IA.gemini import ask_gemini

starting = ask_gemini(
    "Despierta JAI. siempre saluda. di la hora y el clima"
)
print(starting)
speak(starting)

def app():
    while tools.system_tools.jarvis_active:

        input_user = listen()

        if input_user is None:
            continue

        input_user = input_user.lower().strip()
        input_user = unidecode(input_user)

        print("TU: ", input_user)
    
        answer = ask_gemini(input_user)
        print(answer)
        speak(answer)

if __name__ == "__main__":
    app()