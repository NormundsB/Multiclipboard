
from urllib import response
import requests


API_KEY = "0f6783f913176cdfd77be51a2352cb78"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


city = input("Enter city name: ")
request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data["weather"][0]["description"]
    print(weather)
    temperature = round(data["main"]["temp"]-273.15, 2)
    print(f"Temperature in {city} is {temperature}")
else:
    print("Invalid city name")
