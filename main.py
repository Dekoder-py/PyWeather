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

TOMORROW_IO_KEY = getenv("TOMORROW_IO_API")
location = "auckland"
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
    condition = weather_codes[values["weatherCode"]]
    print(f"The temperature in {location} is {values['temperature']}\u00b0C")
    print(f"It is {condition}.")
    display_weather_art()

else:
    print(response)
