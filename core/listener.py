import speech_recognition as sr

def listen():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='pt-BR')
        print("Você:", query)
        return query.lower()

    except:
        print("Erro ao reconhecer voz")
        return ""
