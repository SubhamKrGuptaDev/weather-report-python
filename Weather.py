import requests
import os

# API Key Calling
apiKey = "51cd1f2b14a22998a607a7f2d29ca176"


location = input("Enter City name which city you have to search weather report : ")
apiLink = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+apiKey

apiData = requests.get(apiLink)

apiDataJson = apiData.json()

if apiDataJson['cod'] == 404:
    print("Wrong Coty name {} please check your City and Try again".format(location))
else: 
    # Filter Weather Report
    # Main Reports 
    weather_main = apiDataJson['weather'][0]['main']
    weather_description = apiDataJson['weather'][0]['description']

    # Weather temperature
    weather_temp = ((apiDataJson['main']['temp']) - 273.15)
    weather_temp_min = ((apiDataJson['main']['temp_min']) - 273.15)
    weather_temp_max = ((apiDataJson['main']['temp_max']) - 273.15)

    # Rain Volume
    # weather_rain = apiDataJson['rain']['1h']

    # Weather Wind
    weather_wind_speed = apiDataJson['wind']['speed']

    # Weather Cloud
    weather_clouds = apiDataJson['clouds']['all']

    # Print Seaction
    print("{} Weather main Report : {} | Description : {}".format(location,weather_main,weather_description))
    print("{} Weather Temperature Report : ".format(location))
    print("{} Average Temperature : {} Celsius".format(location,weather_temp))
    print("{} Min Temperature : {} Celsius".format(location,weather_temp_min))
    print("{} Max Temperature : {} Celsius".format(location,weather_temp_max))

    print("{} Weather Wind Speed : {} meter/sec".format(location,weather_wind_speed))
    print("{} Weather Clouds are {}%".format(location,weather_clouds))

    if(weather_clouds > 70):
        print("Bad Weather")
    elif(weather_clouds > 40):
        print("Normal Weather")
    else:
        print("Bad Weather")