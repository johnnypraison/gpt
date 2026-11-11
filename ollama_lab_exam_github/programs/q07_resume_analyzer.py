import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

try:
    with open("resume.txt", "r", encoding="utf-8") as f:
        resume = f.read()
except FileNotFoundError:
    print("Create resume.txt in this folder first.")
    raise SystemExit
prompt = "Identify skills, qualifications, profile summary and improvements. Do not invent facts: " + resume
print(ask_ollama(prompt))
