"""
This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager
classes to achieve the program requirements.
"""

# import json
import logging
from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

# Set up logging
logging.basicConfig(
    level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_flights(target_destination):
    """
    Get flights for a given destination.
    """
    flight_search = FlightSearch()
    tomorrow = datetime.now() + timedelta(days=1)
    # just doing 1 month for now
    six_month_from_today = datetime.now() + timedelta(days=1 * 30)
    flights = []

    departure_date = tomorrow
    while departure_date <= six_month_from_today:
        # assume 7 days for now
        for days in range(7, 8):
            return_date = departure_date + timedelta(days=days)
            logging.debug(
                "  Checking dates: %s %s",
                departure_date.strftime("%Y-%m-%d"),
                return_date.strftime("%Y-%m-%d"),
            )
            new_flights = flight_search.search_flights(
                origin_city_code="BHM",
                destination_city_code=target_destination["iataCode"],
                from_time=departure_date,
                to_time=return_date,
            )
            if new_flights:
                flights.extend(new_flights)
        departure_date += timedelta(days=1)

    return flights


data = DataManager()
# print(json.dumps(data.destination_data, indent=4))

# # fill in missing IATA codes
for destination in data.destination_data:
    if "iataCode" not in destination:
        city_name = destination["city"]
        iata_code = FlightSearch().get_city_code(city_name)
        if iata_code:
            destination["iataCode"] = iata_code
            data.update_destination(destination["id"], {"iataCode": iata_code})
            logging.debug(
                "Updated %s with IATA code %s (%d/%d = %.2f%%)",
                city_name,
                iata_code,
                data.destination_data.index(destination) + 1,
                len(data.destination_data),
                (data.destination_data.index(destination) + 1)
                / len(data.destination_data)
                * 100,
            )
        else:
            logging.error("Failed to get IATA code for %s", city_name)
    flight_list = get_flights(destination)
    if flight_list:
        logging.debug(
            "Found flights for %s: %d (%.2f%% of destinations)",
            destination["city"],
            len(flight_list),
            (len(flight_list) / len(data.destination_data)) * 100,
        )
        lowest_flight = min(flight_list, key=lambda f: f.price)
        highest_flight = max(flight_list, key=lambda f: f.price)
        average_price = sum(f.price for f in flight_list) / len(flight_list)
        logging.info(
            "Lowest price flight for %s: %r", destination["city"], lowest_flight
        )
        logging.info(
            "Highest price flight for %s: %r", destination["city"], highest_flight
        )
        logging.info(
            "Average price flight for %s: %.2f", destination["city"], average_price
        )
        if (
            "lowestPrice" not in destination
            or lowest_flight.price < destination["lowestPrice"]
        ):
            logging.info(
                "Lowest price for %s has changed from %s to %s",
                destination["city"],
                destination.get("lowestPrice"),
                lowest_flight.price,
            )
            NotificationManager().send_sms(
                (
                    f"Low price alert! Only ${lowest_flight.price} to fly from BHM to "
                    f"{destination['city']} from {lowest_flight.departure_date} to "
                    f"{lowest_flight.return_date}."
                )
            )
        # Update the destination data with the new flight prices
        data.update_destination(
            destination["id"],
            {
                "lowestPrice": lowest_flight.price,
                "highestPrice": highest_flight.price,
                "averagePrice": average_price,
            },
        )
        logging.debug("Updated %s with flight data", destination["city"])
    else:
        logging.debug("No flights found for %s", destination["city"])
