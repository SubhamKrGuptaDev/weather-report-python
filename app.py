import requests
import os

# ------------ FLASK ----------------

from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World"

@app.route('/city/<string:n>')
def city(n):
    location = str(n)
    apiKey = "51cd1f2b14a22998a607a7f2d29ca176"
    apiLink = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+apiKey
    apiData = requests.get(apiLink)
    apiDataJson = apiData.json()

    if apiDataJson['cod'] == '404':
        return f"Couldn't find your location - {location} \nPlease check the entered location and try again"
    else: 
        # Filter Weather Report
        # Main Reports 
        weather_main = apiDataJson['weather'][0]['main']
        weather_description = apiDataJson['weather'][0]['description']

        # Weather temperature
        weather_temp = ((apiDataJson['main']['temp']) - 273.15)
        weather_feel = ((apiDataJson['main']['feels_like']) - 273.15)
        weather_temp_min = ((apiDataJson['main']['temp_min']) - 273.15)
        weather_temp_max = ((apiDataJson['main']['temp_max']) - 273.15)

        # Rain Volume

        weather_rain = ""

        try:
            weather_rain = apiDataJson['rain']['3h']
        except:
            pass

        # Weather Wind
        weather_wind_speed = apiDataJson['wind']['speed']

        # Weather Cloud
        weather_clouds = apiDataJson['clouds']['all']

        results = {
            "current_weather": weather_main,
            "weather_description": weather_description,
            "temp_current": round(weather_temp, 2),
            "temp_feels_like": round(weather_feel, 2),
            "temp_min": round(weather_temp_min, 2),
            "temp_max": round(weather_temp_max, 2),
            "rain_3h": weather_rain,
            "wind_speed": weather_wind_speed,
            "cloudiness": weather_clouds
        }

    return jsonify(results)




if __name__ == "__main__":
    app.run(debug=True)
