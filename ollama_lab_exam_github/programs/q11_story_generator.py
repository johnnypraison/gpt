import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

topic = input("Enter story topic: ")
genre = input("Enter genre: ")
audience = input("Enter target audience: ")
prompt = f"Write a short story about {topic}, genre {genre}, for {audience}."
result = ask_ollama(prompt)
print(result)
with open("story.txt", "w", encoding="utf-8") as f:
    f.write(result)
