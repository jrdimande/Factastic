import requests
from src.apis.constants import URL

def generate_random_facts():
    # Get a random fact from the API and return the text
    response = requests.get(URL)

    if response.ok:
        fact_data = response.json()
        fact = fact_data["text"]
        return fact
    return "No interner connection"




