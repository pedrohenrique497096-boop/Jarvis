from core.listener import listen
from core.voice import speak
from core.brain import ask_jarvis
import os
import webbrowser

def executar_comando(query):
    
    if "abrir youtube" in query:
        webbrowser.open("https://youtube.com")

    elif "abrir google" in query:
        webbrowser.open("https://google.com")

    elif "abrir chrome" in query:
        os.system("start chrome")

    elif "hora" in query:
        from datetime import datetime
        hora = datetime.now().strftime("%H:%M")
        speak(f"Agora são {hora}")

    elif "pesquisar" in query:
        termo = query.replace("pesquisar", "")
        webbrowser.open(f"https://www.google.com/search?q={termo}")

    else:
        resposta = ask_jarvis(query)
        speak(resposta)


if __name__ == "__main__":
    speak("Jarvis iniciado")

    while True:
        query = listen()

        if query != "":
            executar_comando(query)
