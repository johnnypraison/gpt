import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

text = input("Enter long paragraph: ")
result = ask_ollama("Summarize this text and list its main ideas: " + text)
print(result)
with open("summary.txt", "w", encoding="utf-8") as f:
    f.write(result)
