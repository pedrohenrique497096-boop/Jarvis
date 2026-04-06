import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("🎤 Ouvindo...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio, language="pt-BR")
        print("Você:", command)
        return command.lower()

    except sr.UnknownValueError:
        print("Não entendi...")
        return ""

    except sr.RequestError:
        print("Erro de conexão")
        return ""
