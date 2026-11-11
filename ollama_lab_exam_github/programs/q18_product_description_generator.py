import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

product = input("Enter product name: ")
features = input("Enter product features: ")
customers = input("Enter target customers: ")
prompt = f"Write an attractive description for {product}. Features: {features}. Target customers: {customers}."
result = ask_ollama(prompt)
print(result)
with open("product_description.txt", "w", encoding="utf-8") as f:
    f.write(result)
