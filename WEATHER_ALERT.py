import requests
from twilio.rest import Client

# Replace YOUR_API_KEY with your OpenWeatherMap API key
url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=YOUR_API_IDS'

# Replace YOUR_TWILIO_ACCOUNT_SID, YOUR_TWILIO_AUTH_TOKEN, and YOUR_TWILIO_PHONE_NUMBER with your Twilio credentials
account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
client = Client(account_sid, auth_token)

city = input("Enter city name: ")
response = requests.get(url.format(city))

if response.status_code == 200:
    data = response.json()
    temp = data['main']['temp']
    description = data['weather'][0]['description']
    humidity = data['main']['humidity']
    wind_speed = data['wind']['speed']
    print("Temperature: {}°C".format(temp))
    print("Description: {}".format(description))
    print("Humidity: {}%".format(humidity))
    print("Wind Speed: {} m/s".format(wind_speed))

    # Set the threshold for temperature, humidity and wind speed
    temp_threshold = 30
    humidity_threshold = 80
    wind_speed_threshold = 10

    # Check if any threshold is exceeded and send a text message if it is
    if temp > temp_threshold:
        message = client.messages.create(
            body="ALERT: High temperature in {}! Temperature: {}°C".format(city, temp),
            from_='YOUR_TWILIO_PHONE_NUMBER',
            to='YOUR_TWILIO_Verified_Caller_IDs_NUMBER'
        )
        print(message.sid)
    elif humidity > humidity_threshold:
        message = client.messages.create(
            body="ALERT: High humidity in {}! Humidity: {}%".format(city, humidity),
            from_='YOUR_TWILIO_PHONE_NUMBER',
            to='YOUR_TWILIO_Verified_Caller_IDs_NUMBER'
        )
        print(message.sid)
    elif "rain" in description.lower():
        message = client.messages.create(
            body="ALERT: Rainy weather in {}! Description: {}".format(city, description),
            from_='YOUR_TWILIO_PHONE_NUMBER',
            to='YOUR_TWILIO_Verified_Caller_IDs_NUMBER'
        )
        print(message.sid)
    elif temp < 10:
        message = client.messages.create(
            body="ALERT: Cold weather in {}! Temperature: {}°C".format(city, temp),
            from_='YOUR_TWILIO_PHONE_NUMBER',
            to='YOUR_TWILIO_Verified_Caller_IDs_NUMBER'
        )
        print(message.sid)
    elif temp > 20:
        message = client.messages.create(
            body="ALERT: Warm weather in {}! Temperature: {}°C".format(city, temp),
            from_='YOUR_TWILIO_PHONE_NUMBER',
            to='YOUR_TWILIO_Verified_Caller_IDs_NUMBER'
        )
        print(message.sid)
    elif wind_speed > wind_speed_threshold:
        message = client.messages.create(
            body="ALERT: High wind speed in {}! Wind Speed: {} m/s".format(city, wind_speed),
            from_='YOUR_TWILIO_PHONE_NUMBER',
            to='YOUR_TWILIO_Verified_Caller_IDs_NUMBER'
        )
        print(message.sid)
else:
    print("Error fetching weather data: {}".format(response.text))
