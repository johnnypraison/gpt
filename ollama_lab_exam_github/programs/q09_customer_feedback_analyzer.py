import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

feedback = input("Enter customer feedback: ")
prompt = "Identify complaint or appreciation, classify Positive/Negative/Neutral, and suggest an action: " + feedback
print(ask_ollama(prompt))
