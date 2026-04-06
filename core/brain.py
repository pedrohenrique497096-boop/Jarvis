import requests

def ask_jarvis(prompt):
    try:
        url = "http://localhost:11434/api/generate"

        data = {
            "model": "phi",
            "prompt": f"Responda em português como um assistente inteligente: {prompt}",
            "stream": False
        }

        response = requests.post(url, json=data)
        return response.json()["response"]

    except:
        return "Erro ao acessar o cérebro."
