"""
This script demonstrates how to fetch data from an API, save it to a JSON file,
and then read and print the data from that file.
"""

# The 'json' module provides functions for parsing and generating JSON data.
import json

# The'requests'module is used for making HTTP requests to interact with web
# APIs.
# Note: 'requests' is not included with Python by default. Install it using:
# 'pip install requests'.
import requests

url = 'https://api.open-meteo.com/v1/forecast?latitude=35.6895&longitude=139.6917&current_weather=true'

# Fetch data from the API
response = requests.get(url, timeout=10)

# Save the fetched data to a JSON file
with open('weather_data.json', 'w', encoding='utf-8') as outfile:
    json.dump(response.json(), outfile, sort_keys=True, indent=4)

# Read and print the data from the JSON file
with open('weather_data.json', 'r', encoding='utf-8') as j:
    json_data = json.load(j)
    print(json_data)
