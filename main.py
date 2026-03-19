
import os
import requests

api_key = os.environ.get("api_key")
account_sid = os.environ.get("account_sid")
auth_token = os.environ.get("auth_token")
from twilio.rest import Client




client = Client(account_sid,auth_token)

parameters = {
                "lat":44.39071,
                "lon":7.54828,
                "appid":api_key,
                "cnt": 4,
}

data = requests.get(url="https://api.openweathermap.org/data/2.5/forecast?",params=parameters)

print(data.raise_for_status())

weather_data = data.json()
print(weather_data)

forecast_code = []
rain = True

while rain:
    for element in weather_data["list"]:
        forecast_code.append(element["weather"][0]["id"])
    for n in forecast_code:
        if n < 700:
            message = client.messages.create(
                body="It will rain today",
                from_="+15706336955",
                to="+393318524660"
            )
            print(message.status)
            rain = False
    break
