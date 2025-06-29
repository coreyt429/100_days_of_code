import os
import requests
from requests.auth import HTTPBasicAuth


SHEETY_PRICES_ENDPOINT = os.getenv("SHEETY_ENDPOINT_FLIGHTS")
SHEETY_ENDPOINT_USERS = os.getenv("SHEETY_ENDPOINT_USERS")

print(f"SHEETY_PRICES_ENDPOINT: {SHEETY_PRICES_ENDPOINT}")
print(f"SHEETY_ENDPOINT_USERS: {SHEETY_ENDPOINT_USERS}")

class DataManager:

    def __init__(self):
        self._api_key = os.getenv("SHEETY_API_KEY")
        self._endpoint = os.getenv("SHEETY_ENDPOINT_FLIGHTS")
        self._header = {
            "Authorization": f"Bearer {self._api_key}",
            "Content-Type": "application/json",
        }
        self.destination_data = {}

    def get_destination_data(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        # Try importing pretty print and printing the data out again using pprint() to see it formatted.
        # pprint(data)
        return self.destination_data

    # In the DataManager Class make a PUT request and use the row id from sheet_data
    # to update the Google Sheet with the IATA codes. (Do this using code).
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
    
    def get_emails(self):
        # Use the Sheety API to GET all the data in that sheet and print it out.
        response = requests.get(url=SHEETY_ENDPOINT_USERS)
        data = response.json()
        return data["users"]
