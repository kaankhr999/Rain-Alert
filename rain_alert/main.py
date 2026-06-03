import requests
import os
from twilio.rest import Client

api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

weather_params = {
    "lat": 39.89,
    "lon": 32.71,
    "cnt": 4,
    "appid": api_key
}

owm_api_endpoint = f"https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(owm_api_endpoint, params=weather_params)
response.raise_for_status()

if response.status_code == 200:
    weather_data = response.json()

weather_data_list = weather_data["list"]

rain = False

for time in weather_data_list:
    if time["weather"][0]["id"] < 700:
        rain = True

if rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
    .create(
        body="It will rain today, do not forget to bring an umbrella ☔",
        from_="whatsapp:+14155238886",
        to="whatsapp:+905340859005"
    )

    print(message.status)