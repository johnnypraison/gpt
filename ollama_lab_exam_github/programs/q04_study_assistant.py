import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

topic = input("Enter academic topic: ")
prompt = f"Explain {topic} simply, give one example and three key points."
print(ask_ollama(prompt))
