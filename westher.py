import requests
import os

# API Key Calling
apiKey = "51cd1f2b14a22998a607a7f2d29ca176"

location = input("Enter City name for which you want to find the weather report: ").lower()

apiLink = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+apiKey

apiData = requests.get(apiLink)

apiDataJson = apiData.json()

#print(apiDataJson)

if apiDataJson['cod'] == '404':
    print("Couldn't find your location - {} \nPlease check the entered location and try again".format(location))
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

#print('{:s}'.format('\u0332'.join('\nRain details\n'))[:-1])

    # Print Seaction
    print("\nWeather report for {:s}".format('\u0332'.join(location.capitalize())))
    print("Current weather description: {}".format(weather_description.capitalize()))
    
    print('{:s}'.format('\u0332'.join('\nTemperature details\n'))[:-1])
    
    print("Current Temperature: {} Celsius".format(round(weather_temp, 2)))
    print("Feel\'s like: {} Celsius".format(round(weather_feel, 2)))
    print("Average Temperature : {} Celsius".format(round(weather_temp, 2)))
    print("Min Temperature : {} Celsius".format(round(weather_temp_min, 2)))
    print("Max Temperature : {} Celsius".format(round(weather_temp_max, 2)))

    if (weather_rain):
        
        print('{:s}'.format('\u0332'.join('\nRain details\n'))[1:-1])

        print("Rain volume for the last 1 hour: {}mm".format(weather_rain))
    else:
        print('{:s}'.format('\u0332'.join('\nWind and Cloud details\n'))[:-1])

        print("Wind Speed: {} meter/sec".format(weather_wind_speed))
        print("Cloudiness %: {}%".format(weather_clouds))

        if(weather_clouds > 70):
            print("\nAs Cloudiness % is high, kindly refrain from travelling using 2-wheeler\nHave a safe journey\n")
        else:
            print("\nHave a safe journey\n")