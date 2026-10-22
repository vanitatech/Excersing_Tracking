import requests
import datetime
import os

#Nutritionix API
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
HEADERS = {
    "x-app-id": os.environ["ENV_NIX_APP_ID"],
    "x-app-key": os.environ["ENV_NIX_API_KEY"],
}

#Sheety API
SHEETY_ENDPOINT = os.environ["ENV_SHEETY_ENDPOINT"]

#Ask user what excercise they did
input_text = input("Tell me which exercise you did: ")

exercise_data = {
    "query": input_text
}

# Send the excercise data to the Nutritionix API
response = requests.post(url=EXERCISE_ENDPOINT, json=exercise_data, headers=HEADERS)
print(response.status_code)
if response.ok:
    exercise_result = response.json()
    exercises = exercise_result["exercises"]

    # Get the current date and time
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Send each exercise to the Sheety API
    for exercise in exercises:
        sheety_data = {
            "workout": {
                "date": current_date,
                "time": current_time,
                "exercise": exercise["name"],
                "duration": exercise["duration_min"],
                "calories": exercise["nf_calories"]
            }
        }
        sheety_response = requests.post(url=SHEETY_ENDPOINT, json=sheety_data)

        if sheety_response.ok:
            print("Successfully added exercise to Sheety.")
        else:
            print("Failed to add exercise to Sheety:", sheety_response.status_code)
            print(sheety_response.text)

else:
    print("Failed to get exercise data from Nutritionix:", response.status_code)
    print(response.text)
