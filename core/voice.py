import pyttsx3

engine = pyttsx3.init()

# Configurar voz (português se disponível)
voices = engine.getProperty('voices')
for voice in voices:
    if "brazil" in voice.name.lower() or "portuguese" in voice.name.lower():
        engine.setProperty('voice', voice.id)

engine.setProperty('rate', 180)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()
