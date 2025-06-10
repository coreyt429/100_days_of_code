"""
This module is responsible for sending notifications with the deal flight details.
"""

import os
import dotenv
import requests
from flight_data import FlightData


class FlightSearch:
    """
    This class is responsible for searching for flights using the Amadeus API.
    """

    def __init__(self):
        dotenv.load_dotenv("../.env")
        self._api_key = os.getenv("AMADEUS_API_KEY")
        self._api_secret = os.getenv("AMADEUS_API_SECRET")
        self._base_url = os.getenv("AMADEUS_API_BASE_URL")
        self.access_token = None
        self._get_access_token()

    def _get_access_token(self):
        """
        Get the access token from the Amadeus API.
        """
        url = f"{self._base_url}/v1/security/oauth2/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded"}
        data = {
            "grant_type": "client_credentials",
            "client_id": self._api_key,
            "client_secret": self._api_secret,
        }
        response = requests.post(url, headers=headers, data=data, timeout=60)
        if response.status_code == 200:
            self.access_token = response.json()["access_token"]
            print(f"Access token: {self.access_token}")
            return self.access_token
        return None

    def get_city_code(self, city_name):
        """
        Get the IATA code for a city using the Amadeus API.
        """
        url = f"{self._base_url}/v1/reference-data/locations/cities"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }
        params = {"include": "AIRPORTS", "keyword": city_name, "max": 2}
        response = requests.get(url, headers=headers, params=params, timeout=60)
        if response.status_code == 200:
            data = response.json()
            if data["data"]:
                city_code = data["data"][0]["iataCode"]
                return city_code
            print(f"No city code found for {city_name}")
            return None
        return None

    def search_flights(
        self, origin_city_code, destination_city_code, from_time, to_time
    ):
        """
        Search for flights using the Amadeus API.
        """
        url = f"{self._base_url}/v2/shopping/flight-offers"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json",
        }
        query = {
            "originLocationCode": origin_city_code,
            "destinationLocationCode": destination_city_code,
            "departureDate": from_time.strftime("%Y-%m-%d"),
            "returnDate": to_time.strftime("%Y-%m-%d"),
            "adults": 2,
            "nonStop": "false",
            "currencyCode": "USD",
            "max": "100",
        }
        response = requests.get(url, headers=headers, params=query, timeout=60)
        if response.status_code == 200:
            flights = []
            for flight in response.json()["data"]:
                flight_data = FlightData(
                    origin_airport=flight["itineraries"][0]["segments"][0]["departure"][
                        "iataCode"
                    ],
                    destination_airport=flight["itineraries"][0]["segments"][-1][
                        "arrival"
                    ]["iataCode"],
                    departure_date=flight["itineraries"][0]["segments"][0]["departure"][
                        "at"
                    ],
                    return_date=flight["itineraries"][-1]["segments"][-1]["arrival"][
                        "at"
                    ],
                    price=flight["price"]["grandTotal"],
                )
                flights.append(flight_data)
            return flights
        return []
