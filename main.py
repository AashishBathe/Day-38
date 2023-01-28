import requests
import datetime as dt
import os

APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")

INPUT_TXT = input("Enter the exercise you performed: ")

TODAY = dt.datetime.now()
DATE = TODAY.strftime("%d/%m/%Y")
TIME = TODAY.strftime("%X")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json"
}

param = {
    "query": INPUT_TXT,
    "gender": "male",
    "weight_kg": 45,
    "height_cm": 165,
    "age": 20
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=param, headers=headers)
data = response.json()
print(data)

for entity in data["exercises"]:
    exercise_params = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": entity["name"].title(),
            "duration": entity["duration_min"],
            "calories": entity["nf_calories"]
        }
    }
    
    exer_headers = {
        "Authorization": os.environ.get("Authorization")
    }
    add_row = requests.post(url="https://api.sheety.co/d286618cf163e11a39db03ed83a32547/myWorkouts/workouts",
                            json=exercise_params, headers=exer_headers)
    print(add_row.text)
