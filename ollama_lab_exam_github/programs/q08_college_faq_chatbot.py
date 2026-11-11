import requests

def ask_ollama(prompt):
    url = "http://localhost:11434/api/generate"
    data = {"model": "llama3.2", "prompt": prompt, "stream": False}
    response = requests.post(url, json=data, timeout=180)
    response.raise_for_status()
    return response.json()["response"]

faqs = {
    "admission": "Contact the college admission office.",
    "courses": "The college offers undergraduate and postgraduate courses.",
    "library": "Check the college notice board for current library timings.",
    "examination": "The examination cell publishes the schedule."
}
question = input("Ask a college question: ")
prompt = ("Answer only from this FAQ data. If unavailable, say information is not available. "
          + str(faqs) + " Question: " + question)
print(ask_ollama(prompt))
