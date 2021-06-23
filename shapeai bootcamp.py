from time import strftime

import webrequests
# import os
from datetime import datetime

api_key: str = '622abb51f858e8312deb2c2d65324554'
location = input("enter the city name:")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q=" + location + "&appid=" + api_key
api_link = webrequests.get(complete_api_link)
api_data= api_link.json()

#create variables to store and display data
temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
datetime: str = datetime.now().strftime("%d %b %Y || %I:%M:%S %P")

print("**********************")
print("Weather States for - {} || {}".format(location.upper(), datetime))
print("***********************")

print("current temprature is: {:.2f} deg C".format(temp_city))
print("current weather desc :", weather_desc)
print("current humidity      :", hmdt, '%')
print("current wind speed     :", wind_spd, 'kmph')
