import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

topic = input("Enter topic: ")
result = ask_ollama(f"Generate five question-and-answer flashcards about {topic}.")
print(result)
with open("flashcards.txt", "w", encoding="utf-8") as f:
    f.write(result)
