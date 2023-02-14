import requests

BASE = "http://127.0.0.1:5000/"

while True:
    user_input = input("Press Enter to get a random word...")

    response = requests.get(BASE + "get word")
    print(response.json())
