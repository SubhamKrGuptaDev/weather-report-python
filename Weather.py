import requests

# API Key Calling
apiKey = "51cd1f2b14a22998a607a7f2d29ca176"

print("***** Welcome To Ployify Weather Report Service *****\n")

name = input("Enter Your Name : ")

while (True):
    try:
        print("\n")
        print("Enter 1 For Searching Your Current City Weather : ")
        print("Enter 2 For 'EXIT' : ")
        userChoice = int(input("Enter Your Choice : "))
        if userChoice == 1:
            # Input By User
            location = input("Enter City name which city you have to search weather report : ")

            # Link Generate 
            apiLink = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+apiKey

            # If Exception handel
            try:
                apiData = requests.get(apiLink)

                apiDataJson = apiData.json()

                # If City Not Found
                if apiDataJson['cod'] == 404:
                    print("Wrong City name {} please {} check your City and Try again\n".format(location,name))
                else: 
                    # Filter Weather Report
                    # Main Reports 
                    weather_main = apiDataJson['weather'][0]['main']
                    weather_description = apiDataJson['weather'][0]['description']

                    # Weather temperature
                    weather_temp = round(((apiDataJson['main']['temp']) - 273.15),3)
                    weather_temp_min = round(((apiDataJson['main']['temp_min']) - 273.15),3)
                    weather_temp_max = round(((apiDataJson['main']['temp_max']) - 273.15),3)

                    # Rain Volume
                    # weather_rain = apiDataJson['rain']['1h']

                    # Weather Wind
                    weather_wind_speed = apiDataJson['wind']['speed']

                    # Weather Cloud
                    weather_clouds = apiDataJson['clouds']['all']

                    # Filter Weather to choice transportation for User Section
                    # Clear Section
                    print("\n")
                    print("weather Report -> '{}' || Description -> '{}'".format(weather_main,weather_description))
                    if weather_main == 'Clear':
                        print(f"Current Weather is Clear sky {name} You can use any Transportation")
                    # Mist Section
                    elif weather_main == 'Mist':
                        print("The road is cloaked in mist you can use metro or bus")
                    # Smoke Section
                    elif weather_main == 'Smoke':
                        print("Location covered in thick smog  You can use the bus or metro")
                    # Haze Section
                    elif weather_main == 'Haze':
                        print("Hazy weather you can use metro")
                    # Fog Section
                    elif weather_main == 'Fog':
                        print("It's a foggy morning  You can use the metro")
                    # Sand Section
                    elif weather_main == 'Sand':
                        print("Sandy weather detected  Not safe to travel.")
                    # Dust Section
                    elif weather_main == 'Dust':
                        print("Alert dusty air is moving towards your location  Not safe to travel.")
                    # Ash Section
                    elif weather_main == 'Ash':
                        print("Volcanic ash in the air predicted.")
                    # Squall Section
                    elif weather_main == 'Squall':
                        print("Snow squalls and high winds have been forecasted  Not safe to travel.")
                    # Tornado Section
                    elif weather_main == 'Tornado':
                        print("A tornado is fuming immediately rush to a safer location  Not safe to travel.")
                    # Cloud Section
                    elif weather_main == 'Clouds':
                        if weather_description == 'few clouds':
                            print("it's perfectly sunny,can opt any mode of transportation.")
                        elif weather_description == 'scattered clouds':
                            print("its partly sunny,you can use any of the transportation as per your convenience.")
                        elif weather_description == 'broken clouds':
                            print("Chances of rainfall ,try travelling by car ,metro or bus")
                        elif weather_description == 'overcast clouds':
                            print("There are high chances to rain, therefore you should take car, metro or bus")
                        else:
                            pass 

                    # Snow section
                    elif weather_main == 'Snow':
                        if weather_description == 'light snow':
                            print("User can use any tranportation method.")
                        elif weather_description == 'Snow':
                            print("User is recommended to use any transportation method except 2 wheeler.")
                        elif weather_description == 'Heavy snow':
                            print("User is recommended to use only 4 wheeler.")
                        elif weather_description == 'Sleet':
                            print("User is recommended not to travel but if it's necessary only use 4 wheeler.")
                        elif weather_description == 'Light shower sleet':
                            print("User is recommended to use only 4 wheelers.")
                        elif weather_description == 'Shower sleet':
                            print("User is recommended to use 4 wheeler and maintain low speeed.")
                        elif weather_description == 'Light rain and snow':
                            print("User is recommended to use only 4 wheeler.")
                        elif weather_description == 'Rain and snow':
                            print("User is recommended to use only 4 wheeler.")
                        elif weather_description == 'Light shower snow':
                            print("User can use any type of transportation but 4 wheeler is recommended.")
                        elif weather_description == 'Shower snow':
                            print("User is recommended to use 4 wheeler but can also use 2 wheeler.")
                        elif weather_description == 'Heavy shower snow':
                            print("user is recommended to use 4 wheeler but can also use 2 wheeler.")
                        else:
                            pass

                    # Rain Seation
                    elif weather_main == 'Rain':
                        if weather_description == 'light rain':
                            print("it might Rain today do not forget you Umbrella!!")
                        elif weather_description == 'moderate rain':
                            print("Rain is Expected! Make sure to take your umbrella / Raincoat.")
                        elif weather_description == 'heavy intensity rain':
                            print("Avoid use of Two Wheeler ( It might not be safe due to heavy Rain ).")
                        elif weather_description == 'very heavy rain':
                            print("heavy Rain Expected.")
                        elif weather_description == 'extreme rain':
                            print("Avoid use of Two wheeler. Suggested use of public transport , cab or car.")
                        elif weather_description == 'freezing rain':
                            print("freezing rain ⚠️ Use of Covered Transport means is Highly Suggested ")
                        elif weather_description == 'light intensity shower rain':
                            print("Sudden short rain expected Recommended use of Raincoat for Two Wheeler.")
                        elif weather_description == 'shower rain':
                            print("Avoid use of Two wheeler or Precede with precaution.")
                        elif weather_description == 'heavy intensity shower rain':
                            print("Avoid Two Wheelers⚠️ Suggested use of Public transport or a Cab.")
                        elif weather_description == 'ragged shower rain':
                            print("Precede with Caution ⚠️Raincoat and Umbrella to be kept Handy ")
                        else:
                            pass

                    # Drizzle Section
                    elif weather_main == 'Drizzle':
                        if weather_description == 'light intensity drizzle':
                            print("fine rain, spray, Scotch mist presence expected  two wheeler might not be suggested.")
                        elif weather_description == 'drizzle':
                            print("fine rain, spray, Scotch mist presence expected . two wheeler might not be suggested.")
                        elif weather_description == 'heavy intensity drizzle':
                            print("Scotch mist presence expected . two wheeler might not be suggested ⚠️precede with caution.")
                        elif weather_description == 'light intensity drizzle rain':
                            print("fine rain, spray, Scotch mist presence expected . two wheeler might not be suggested (precede with Raincoat).")
                        elif weather_description == 'drizzle rain':
                            print("suggested to avoid use of two wheeler for travelling ( NOTE : carry Umbrella or Raincoat).")
                        elif weather_description == 'heavy intensity drizzle rain':
                            print("suggested to avoid use of two wheeler for travelling (NOTE:-  Carry Umbrella / Raincoat) ⚠️precede with caution⚠️.")
                        elif weather_description == 'shower rain and drizzle':
                            print("suggested to avoid use of two wheeler for travelling (NOTE:-  Carry Umbrella / Raincoat).")
                        elif weather_description == 'heavy shower rain and drizzle':
                            print("Avoid use of two wheeler ‼️‼️  ⚠️ Suggested  used of public transport (train, metro , bus )cab or car.")
                        elif weather_description == 'shower drizzle':
                            print("fine mist, whereas sprinkles will be present at uneven intervals with rain . suggested use of raincoat if travelling by Two-wheeler.")
                        else:
                            pass

                    # Thunderstorm Section
                    elif weather_main == 'Thunderstorm':
                        if weather_description == 'thunderstorm with light rain':
                            print("Suggested to carry Umbrella / Raincoat")
                        elif weather_description == 'thunderstorm with rain':
                            print("Suggested use of car, cab and public transport")
                        elif weather_description == 'thunderstorm with heavy rain':
                            print("Heavy rainfall with Thunderstorm Expected ⚠️")
                        elif weather_description == 'light thunderstorm':
                            print("thunderstorm expected any means of transport can be used precede with caution  ")
                        elif weather_description == 'thunderstorm':
                            print("Avoid use of Two-Wheeler ")
                        elif weather_description == 'heavy thunderstorm':
                            print("Suggested use of Covered means of Transport (Bus , Car or Cab )")
                        elif weather_description == 'ragged thunderstorm':
                            print("Caution ⚠️ avoid Maximum use of uncovered Transport (i.e. bicycle , two wheelers , motorbikes).")
                        elif weather_description == 'thunderstorm with light drizzle':
                            print("might get some Visibility issues due to Drizzle. precede with Caution if using Two wheelers.")
                        elif weather_description == 'thunderstorm with drizzle':
                            print("Visibility issues due to Drizzle.  Avoid use of Two-wheeler and precede with Caution⚠️.")
                        elif weather_description == 'thunderstorm with heavy drizzle':
                            print("WARNING ‼️ Heavy Drizzle. maximum avoid use of uncovered Vehicle (Suggested to Travel Very Safely).")
                        else:
                            pass
                    else:
                        pass

                    print("\n")
                    print(f"{name} if You Want to See All Details then type YES/NO : ")
                    all_details = input("Enter Your choice : ")
                    if(all_details == 'YES'):
                        # All Weather Details Section
                        print("\n\n*********** Current Weather Total details ****************\n")
                        print("{} Weather main Report : {} | Description : {}".format(location,weather_main,weather_description))
                        print("{} Weather Temperature Report : ".format(location))
                        print("{} Average Temperature : {} Celsius".format(location,weather_temp))
                        print("{} Min Temperature : {} Celsius".format(location,weather_temp_min))
                        print("{} Max Temperature : {} Celsius".format(location,weather_temp_max))

                        print("{} Weather Wind Speed : {} meter/sec".format(location,weather_wind_speed))
                        print("{} Weather Clouds are {}%".format(location,weather_clouds))
                        print("\n\n")
                    elif all_details == 'NO':
                        pass
                    else:
                        print("\n")
                        print(f"Sorry {name} Wrong Input")
            except:
                print("\n")
                print(f"Sorry {name} Please Check your City Name : {location} Not Found Try again\n")
        elif userChoice == 2:
            asciis = chr(2)
            print("\n")
            print(f"{name} {asciis}{asciis}{asciis} Thank You So Much for Using Ployify {asciis}{asciis}{asciis} *** 'Developed by Ployify team' ***\n")
            break
        else:
            print("\n")
            print(f"Sorry {name} Wrong Choice Try again\n")
    except:
        print("\n")
        print(f"Sorry {name} Wrong Input Try Again\n")
