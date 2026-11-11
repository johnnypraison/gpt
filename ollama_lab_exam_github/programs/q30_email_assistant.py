import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

email = input("Enter original email: ")
tone = input("Enter tone (Formal/Friendly/Professional): ")
prompt = f"Write an email reply in {tone} tone with subject, greeting, message and closing. Do not invent facts: {email}"
result = ask_ollama(prompt)
print(result)
with open("email_reply.txt", "w", encoding="utf-8") as f:
    f.write(result)
