# src/fetch_apis.py
import requests
import json
import time
from pathlib import Path
from dotenv import load_dotenv
import os
import schedule
import datetime

# Load environment variables
load_dotenv()
    
OPENWEATHER_KEY = os.getenv("OPENWEATHER_KEY")
AQICN_TOKEN = os.getenv("AQICN_TOKEN")

# Folder to save raw data
OUTDIR = Path("/Users/shreyastk/Documents/smartcity-dashboard/data/raw")
OUTDIR.mkdir(parents=True, exist_ok=True)

# List of cities
cities = [
    {"name":"Mumbai","lat":19.0760,"lon":72.8777},
    {"name":"Delhi","lat":28.7041,"lon":77.1025},
    {"name":"Bengaluru","lat":12.9716,"lon":77.5946},
    {"name":"Chennai","lat":13.0827,"lon":80.2707},
    {"name":"Kolkata","lat":22.5726,"lon":88.3639}
]

# Fetch OpenWeatherMap data
def fetch_weather(lat, lon):
    url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/{lat},{lon}?unitGroup=metric&key={OPENWEATHER_KEY}"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()

# Fetch AQICN air quality data
def fetch_aqi(lat, lon):
    url = f"https://api.waqi.info/feed/geo:{lat};{lon}/?token={AQICN_TOKEN}"
    r = requests.get(url)
    r.raise_for_status()
    return r.json()

# Loop over cities and save data
def job():
    for city in cities:
        print(f"Fetching weather for {city['name']}...")
        weather_data = fetch_weather(city["lat"], city["lon"])
        (OUTDIR/f"{city['name']}_weather.json").write_text(json.dumps(weather_data))
        time.sleep(1)  # avoid API rate limit
        
        print(f"Fetching AQI for {city['name']}...")
        aqi_data = fetch_aqi(city["lat"], city["lon"])
        (OUTDIR/f"{city['name']}_aqi.json").write_text(json.dumps(aqi_data))
        time.sleep(1)
    
    print(f"✅ Data fetching completed for {datetime.datetime.now()}")
    
    print("Storing data in PostgreSQL....")
    os.system("python3 /Users/shreyastk/Documents/smartcity-dashboard/src/store_data.py")

#intializing the start time 
start_time = datetime.datetime.now()
duration = 24

schedule.every(1).hours.do(job)
job()

while True:
    schedule.run_pending()
    time.sleep(30)
    elapsed = (datetime.datetime.now() - start_time).total_seconds() / 3600
    if elapsed >= duration:
        print("✅ 24 hours completed! Fetching stopped.")
        break

#analyzing of data stored 
print("Analyzing the data and storing as CSV file ")
os.system("python3 /Users/shreyastk/Documents/smartcity-dashboard/src/analyze_data.py")
