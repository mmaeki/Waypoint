import requests
import json
from serpapi import GoogleSearch 


# google hotels api

# "Bali Resorts"
loc = input("Enter your location: ")
# "2024-03-06"
checkin = input("Enter your check-in date (YYYY-MM-DD): ")
# "2024-03-07",
checkout = input("Enter your check out date (YYYY-MM-DD): ")
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


# Assuming json_data contains your JSON string
# Extracting hotel names
hotel_names = []

# Extracting hotel names from the brands section
for brand in results.get('brands', []):
    hotel_names.append(brand['name'])
    for child_brand in brand.get('children', []):
        hotel_names.append(child_brand['name'])

# Extracting hotel names from the properties section
for property_data in results.get('properties', []):
    hotel_names.append(property_data['name'])

print(results)



# Weather API

# Implement binary search to convert US city names to their corresponding latitude and longitude values.

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

print(forecastList[0])
# taking first values



# new york 45, -70

# topeka, Kansas 39,-97

#Gemini API KEY: AIzaSyBTsQxRCoRFyhEHBupl3oCNwNwlyfYs2sE


