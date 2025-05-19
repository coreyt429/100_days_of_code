"""
Module to fetch trivia questions from the Open Trivia Database.
"""

import requests


def fetch_data() -> list:
    """Fetch trivia questions from the Open Trivia Database."""
    url = "https://opentdb.com/api.php?amount=10&type=boolean&category=18"
    response = requests.get(url, timeout=5)
    response.raise_for_status()  # Raise an error for bad responses
    data = response.json()
    return data["results"]
