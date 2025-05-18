import requests
from datetime import datetime
from time import sleep

MY_LAT = 33.264179 # Your latitude
MY_LONG = -87.561295 # Your longitude
MY_POS = (MY_LAT, MY_LONG)

def get_iss_position():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])
    return (iss_latitude, iss_longitude)

def iss_overhead(position, iss_position):
    """Check if the ISS is within +5 or -5 degrees of the user's position."""
    for idx, value in enumerate(position):
        if value -5 <= iss_position[idx] <= value + 5:
            continue
        return False
    return True

def get_sunrise_sunset():
    """Get the sunrise and sunset times."""
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    return data["results"]["sunrise"], data["results"]["sunset"]

def is_dark():
    """Check if the current time is between sunrise and sunset."""
    sunrise, sunset = get_sunrise_sunset()
    current_time = datetime.now()
    if current_time.hour >= sunset or current_time.hour <= sunrise:
        return True
    return False



while True:
    #If the ISS is close to my current position
    iss_pos = get_iss_position()
    if iss_overhead(MY_POS, iss_pos):
        # and it is currently dark
        if is_dark():
            # Then send me an email to tell me to look up.
            print("Look up! The ISS is overhead and it's dark.")
        else:
            print("The ISS is overhead, but it's not dark.")
        # I'm skipping the email part for now.
    else:
        print("The ISS is not overhead.")
    sleep(60)  # Wait for 60 seconds before checking again


