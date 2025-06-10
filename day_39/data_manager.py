"""
This module is responsible for sending notifications with the deal flight details.
"""

import os
import logging
import dotenv
import requests


class DataManager:
    """DataManager class to manage destination data."""

    def __init__(self):
        dotenv.load_dotenv("../.env")
        self._api_key = os.getenv("SHEETY_API_KEY")
        self._endpoint = os.getenv("SHEETY_ENDPOINT_FLIGHTS")
        self._header = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }

        self.destination_data = {}
        self.get_destination_data()

    def get_destination_data(self):
        """Method to get destination data from the Google Sheet."""
        response = requests.get(self._endpoint, headers=self._header, timeout=10)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def get_destination(self, _id):
        """Method to get a destination by its ID."""
        for destination in self.destination_data:
            if destination["id"] == _id:
                return destination
        return None

    def update_destination(self, _id, data):
        """Method to update a destination in the Google Sheet."""
        destination = self.get_destination(_id)
        destination.update(data)
        response = requests.put(
            url=f"{self._endpoint}/{_id}",
            headers=self._header,
            json={"price": data},
            timeout=10,
        )
        if response.status_code == 200:
            return True
        logging.debug(
            "Failed to update destination with id %s: %s %s",
            _id, response.status_code, response.text
        )
        return False
