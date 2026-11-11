import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

text = input("Enter paragraph: ")
print(ask_ollama("Extract important keywords, key phrases and main concepts as a bullet list: " + text))
