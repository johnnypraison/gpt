import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

tasks = input("Enter tasks separated by commas: ")
time = input("Enter available time: ")
prompt = f"Create a daily schedule with time slots for these tasks: {tasks}. Available time: {time}."
print(ask_ollama(prompt))
