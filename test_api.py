import requests
import json

# Define the URL of the Flask API
url = "http://127.0.0.1:5000/predict"

# Define multiple test cases
test_cases = [
    {
        "PetID": 1,
        "PetType": "Cat",
        "Breed": "Persian",
        "AgeMonths": 24,
        "Color": "Brown",
        "Size": "Small",
        "WeightKg": 5.5,
        "Vaccinated": 1,
        "HealthCondition": 0,
        "TimeInShelterDays": 20,
        "AdoptionFee": 100,
        "PreviousOwner": 0
    },
    {
        "PetID": 2,
        "PetType": "Dog",
        "Breed": "Labrador",
        "AgeMonths": 36,
        "Color": "Black",
        "Size": "Large",
        "WeightKg": 30.0,
        "Vaccinated": 0,
        "HealthCondition": 1,
        "TimeInShelterDays": 60,
        "AdoptionFee": 150,
        "PreviousOwner": 1
    }
]

# Send requests for each test case
for i, test_case in enumerate(test_cases):
    response = requests.post(url, headers={"Content-Type": "application/json"}, data=json.dumps([test_case]))
    print(f"Test Case {i + 1}")
    print("Response Status Code:", response.status_code)
    print("Response JSON:", response.json())
    print("\n")
