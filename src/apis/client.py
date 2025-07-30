import requests
from src.apis.constants import URL
from src.storage.saved_facts import load_Facts
from random import choice

saved_facts = load_Facts()

def generate_random_facts():
    # Get a random fact from the API and return the text
    try:
        response = requests.get(URL)

        if response.ok:
            fact_data = response.json()
            fact = fact_data["text"]
            return fact
        return "Resource not  found"
    except requests.exceptions.ConnectionError:
        return choice(saved_facts)