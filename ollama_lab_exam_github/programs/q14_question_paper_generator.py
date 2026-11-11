import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

subject = input("Enter subject: ")
topic = input("Enter topic: ")
count = input("Enter number of questions: ")
prompt = f"Generate {count} questions and answers for {subject} on {topic}."
print(ask_ollama(prompt))
