import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

notes = input("Enter meeting notes: ")
prompt = "Create meeting minutes with summary, decisions and action items. Do not invent details: " + notes
result = ask_ollama(prompt)
print(result)
with open("meeting_minutes.txt", "w", encoding="utf-8") as f:
    f.write(result)
