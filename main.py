from os import getenv

import requests
from dotenv import load_dotenv
from rich import print

load_dotenv()

TOMORROW_IO_KEY = getenv("TOMORROW_IO_API")
location = "auckland"
url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}"
headers = {
    "content-type": "application/json",
    "apikey": TOMORROW_IO_KEY,
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    content = response.json()
    values = content["data"]["values"]
    print(f"The temperature in {location} is {values["temperature"]}")
else:
    print(response)
