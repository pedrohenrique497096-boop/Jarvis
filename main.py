from core.listener import listen
from core.voice import speak
from core.brain import ask_jarvis

from automation.system_control import (
    open_notepad,
    open_chrome,
    open_youtube,
    open_google
)

from automation.mouse_keyboard import (
    write,
    press,
    abrir_pesquisa_windows
)

import time

speak("Jarvis iniciado. Pronto para comandos.")

while True:
    command = listen()

    if command == "":
        continue

    # ENCERRAR
    if "sair" in command or "desligar jarvis" in command:
        speak("Desligando. Até mais.")
        break

    # ABRIR PROGRAMAS
    elif "abrir bloco de notas" in command:
        speak("Abrindo bloco de notas")
        open_notepad()

    elif "abrir chrome" in command:
        speak("Abrindo o Chrome")
        open_chrome()

    elif "abrir youtube" in command:
        speak("Abrindo YouTube")
        open_youtube()

    elif "abrir google" in command:
        speak("Abrindo Google")
        open_google()

    # ESCREVER
    elif "escrever" in command:
        speak("O que você quer que eu escreva?")
        texto = listen()
        write(texto)
        speak("Texto digitado")

    # PESQUISA WINDOWS
    elif "pesquisar" in command:
        speak("O que deseja pesquisar?")
        texto = listen()
        abrir_pesquisa_windows()
        time.sleep(1)
        write(texto)
        press("enter")

    # IA (RESPOSTAS)
    else:
        resposta = ask_jarvis(command)
        speak(resposta)
