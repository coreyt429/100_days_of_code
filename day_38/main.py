import requests
import dotenv
import os
import json
from datetime import datetime
dotenv.load_dotenv('../.env')

NUTRITIONIX_API_KEY = os.getenv('NUTRITIONIX_API_KEY')
NUTRITIONIX_APP_ID = os.getenv('NUTRITIONIX_APP_ID')
SHEETY_API_KEY = os.getenv('SHEETY_API_KEY')
SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')

BASE_URL= 'https://trackapi.nutritionix.com/v2'
excercise_endpoint = f'{BASE_URL}/natural/exercise'

HEADERS = {
    'x-app-id': NUTRITIONIX_APP_ID,
    'x-app-key': NUTRITIONIX_API_KEY,
    'x-remote-user-id': '0',
    'Content-Type': 'application/json'
}

excercise_description = input("Tell me which exercises you did: ")

response = requests.post(
    url=excercise_endpoint,
    json={
        'query': excercise_description
    },
    headers=HEADERS
)
data = response.json()
now = datetime.now()
now_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%H:%M:%S")

HEADERS = {
    "Authorization": f"Bearer {SHEETY_API_KEY}"
}
for exercise in data['exercises']:
    exercise_name = exercise['name']
    duration = exercise['duration_min']
    calories = exercise['nf_calories']
    parameters = {
        'workout': {
            'date': now_date,
            'time': now_time,
            'exercise': exercise_name.title(),
            'duration': duration,
            'calories': calories
        }
    }
    print(f"Exercise: {exercise_name}")
    print(f"Duration: {duration} minutes")
    print(f"Calories burned: {calories} kcal")
    print(f"Date: {now_date}")
    print(f"Time: {now_time}")
    print("-----")
    response = requests.post(
        url=SHEETY_ENDPOINT,
        json=parameters,
        headers=HEADERS
    )
    print(response.status_code, response.text)
    