import requests
from src.apis.constants import URL

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
        return "No internet connection"




