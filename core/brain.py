import requests

def ask_jarvis(prompt):
    try:
        url = "http://localhost:11434/api/generate"

        data = {
            "model": "phi",
            "prompt": f"Responda em português de forma natural e útil: {prompt}",
            "stream": False
        }

        response = requests.post(url, json=data)
        result = response.json()["response"]

        return result

    except:
        return "Erro ao acessar a inteligência local."
