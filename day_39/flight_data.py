"""
This module is responsible for sending notifications with the deal flight details.
"""


class FlightData:
    """
    This class is responsible for storing flight data.
    """

    def __init__(self, **kwargs):
        self.origin_airport = kwargs.get("origin_airport")
        self.destination_airport = kwargs.get("destination_airport")
        self.departure_date = kwargs.get("departure_date")
        self.return_date = kwargs.get("return_date")
        self.price = float(kwargs.get("price", 0))

    def __lt__(self, other):
        return self.price < other.price

    def __str__(self):
        return (
            f"Flight from {self.origin_airport} to {self.destination_airport} on "
            f"{self.departure_date} returning on {self.return_date} for ${self.price}"
        )
