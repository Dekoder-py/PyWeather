from os import getenv

import requests
from dotenv import load_dotenv
from rich import print


def display_weather_art():
    if condition == weather_codes[1000] or condition == weather_codes[1100]:
        print(
            r"""[yellow]
  \   /  
   .-.   
― (   ) ―
   `-’   
  /   \  

[/yellow]"""
        )
    elif condition == weather_codes[1101] or condition == weather_codes[1102]:
        print(
            r"""[grey]

                                
        +++++++                 
      +        +++++++         
     +                 +       
     +                 ++      
   +++                 +++   
 ++                       ++ 
 +                         + 
 ++                      ++ 
   ++++++++++++++++++++++   
                                

[/grey]"""
        )
    else:
        print("No ascii art.")


load_dotenv()

TOMORROW_IO_KEY = getenv("TOMORROW_IO_API") or input("Enter your Tomorrow.io API Key: ")
location = input("Enter a location: ").lower()
url = f"https://api.tomorrow.io/v4/weather/realtime?location={location}"
headers = {
    "content-type": "application/json",
    "apikey": TOMORROW_IO_KEY,
}

response = requests.get(url, headers=headers)

weather_codes = {
    1000: "clear",
    1100: "mostly clear",
    1101: "partly cloudy",
    1102: "mostly cloudy",
}

if response.status_code == 200:
    content = response.json()
    values = content["data"]["values"]

    print(f"Location:  {content['location']['name']}")

    print(f"Current temperature: {values['temperature']}\u00b0C")

    condition = weather_codes[values["weatherCode"]]
    print(f"It is {condition}.")
    display_weather_art()
elif response.status_code == 400:
    print("Invalid Location.")
else:
    print(f"Error: {response}")
