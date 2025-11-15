# src/store_data.py
import json
from pathlib import Path
from sqlalchemy import create_engine,text
from dotenv import load_dotenv
import os
from urllib.parse import quote_plus

load_dotenv()

# PostgreSQL connection setup
password = quote_plus(os.getenv("DB_PASS"))
engine = create_engine(
    f"postgresql+psycopg2://{os.getenv('DB_USER')}:{password}@{os.getenv('DB_HOST')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)

RAW_DIR = Path("/Users/shreyastk/Documents/smartcity-dashboard/data/raw")

def insert_weather_data(city, temperature, humidity, condition, wind_speed):
    query = f"""
        INSERT INTO weather_data (city, temperature, humidity, condition, wind_speed)
        VALUES ('{city}', {temperature}, {humidity}, '{condition}', {wind_speed});
    """
    with engine.begin() as conn:
        conn.execute(text(query))

def insert_aqi_data(city, aqi, pollutant):
    query = f"""
        INSERT INTO aqi_data (city, aqi, dominent_pollutant)
        VALUES ('{city}', {aqi}, '{pollutant}');
    """
    with engine.begin() as conn:
        conn.execute(text(query))

# Loop through the JSON files
for file in RAW_DIR.glob("*_weather.json"):
    city = file.stem.replace("_weather", "")
    data = json.loads(file.read_text())

    try:
        current = data["currentConditions"]
        temp = current.get("temp", None)
        humidity = current.get("humidity", None)
        condition = current.get("conditions", "")
        wind_speed = current.get("windspeed", None)
        insert_weather_data(city, temp, humidity, condition, wind_speed)
        print(f"✅ Inserted weather for {city}")
    except Exception as e:
        print(f"⚠️ Skipped {city} weather: {e}")

for file in RAW_DIR.glob("*_aqi.json"):
    city = file.stem.replace("_aqi", "")
    data = json.loads(file.read_text())

    try:
        aqi = data["data"]["aqi"]
        pollutant = data["data"]["dominentpol"]
        insert_aqi_data(city, aqi, pollutant)
        print(f"✅ Inserted AQI for {city}")
    except Exception as e:
        print(f"⚠️ Skipped {city} AQI: {e}")

print("Storing completed in PostgreSQL")