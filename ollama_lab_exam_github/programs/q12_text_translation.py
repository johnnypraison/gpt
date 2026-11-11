import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

text = input("Enter paragraph: ")
language = input("Enter target language: ")
result = ask_ollama(f"Translate this text into {language}: {text}")
print(result)
with open("translated_text.txt", "w", encoding="utf-8") as f:
    f.write(result)
