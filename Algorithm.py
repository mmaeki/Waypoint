import requests 
import json 

#Google Hotel API (Using serpAPI)
from serpapi import GoogleSearch

#"Bali Resorts"
loc = input("Enter your location: ")
# "2024-03-06"
checkin = input("Enter your check-in date (YYYY-MM-DD): ")
# "2024-03-07",
checkout=  input("Enter your check out date (YYYY-MM-DD): ")
params = {
  "api_key": "c1fed33f43014632d06b27c4a7808bede13b4be6bb258dc774f3ea5d30b6ccf9",
  "engine": "google_hotels",
  "q": loc,
  "hl": "en",
  "gl": "us",
  "check_in_date": checkin,
  "check_out_date": checkout,
  "currency": "USD"
}

search = GoogleSearch(params)
results = search.get_dict()
# for x in range(len(results['hotel_results'])):
#   if(x == "brands"):
#     for y in range(len(results['hotel_results'][x])):
#       print(results['hotel_results'][x][y]['name'])


#Weather API 

#Implement binary search to convert US city names to their corresponding latitude and longitude values.

latitude = int(input("Lat"))
longitude = int(input("long"))

api_token = 'oxGvZawYkOVvhVWBQFmXWdkdgqXBZomI'

url = f'https://api.weather.gov/points/{latitude},{longitude}'

headers = {'token': api_token}

response = requests.get(url, headers=headers)
data = json.loads(response.text)
gridX = 0
gridY = 0
forecastList = []
timeofDay = []

gridX = data['properties']['gridX']
gridY = data['properties']['gridY']
gridID = data['properties']['gridId']

url2 = f'https://api.weather.gov/gridpoints/{gridID}/{gridX},{gridY}/forecast'


headers = {'token': api_token}

response2 = requests.get(url2, headers=headers)
data2 = json.loads(response2.text)
for s in data2['properties']['periods']:
    forecast = s['shortForecast']
    forecastList.append(forecast)
    if len(forecastList) == 2:
        break
for s in data2['properties']['periods']:
    time = s['isDaytime']
    timeofDay.append(time)
    if len(timeofDay) == 2:
        break

print(forecastList[0]) 
#taking first values 
if(timeofDay[0]):
    print("It is daytime")
else:
    print("It is nighttime")  

#new york 45, -70

#topeka, Kansas 39,-97

# openAI Api 

