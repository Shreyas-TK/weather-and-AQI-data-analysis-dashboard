🌆 Smart City Weather & AQI Monitoring Dashboard

End-to-End Data Engineering + Analytics Project

This project is a 24-hour real-time data pipeline that collects weather and AQI data for multiple Indian cities, stores it in PostgreSQL, performs EDA, and visualizes insights in an interactive Tableau Dashboard.
⸻
📌 Project Overview

The goal is to build a Smart City Monitoring System that tracks:
	•	🌡️ Temperature
	•	💧 Humidity
	•	🍃 Wind Speed
	•	🌥️ Weather Conditions
	•	🏭 AQI Levels
	•	🟣 Dominant Pollutant (PM2.5 / PM10)

The system fetches data every 1 hour, stores it for 24 hours, cleans it, and provides a single dashboard with actionable insights for decision-making.

📁 Project Structure
smartcity-dashboard/
│
├── data/
│   ├── raw/              # Raw API JSON files (auto-generated)
│   ├── clean/            # Clean CSVs (aqi.csv, weather.csv)
│
├── src/
│   ├── db_connect.py     # PostgreSQL connection script
│   ├── fetch_apis.py     # Fetches weather & AQI from external APIs
│   ├── store_data.py     # Inserts data into PostgreSQL
│   ├── analyze_data.py   # EDA & data cleaning
│
├── sql/
│   ├── EDA_for_AQI_data.sql
│   ├── EDA_for_weather_data.sql
│   ├── PostgreSQL_query.sql
│
├── dashboard/
│   └── Final_dashboard.twb   # Tableau Dashboard file
│
├── venv/                # Python virtual environment
│
├── requirements.txt     # Project dependencies
│
└── README.md

⚙️ Tech Stack

Languages
	•	Python
	•	SQL (PostgreSQL)
	•	Tableau (Dashboard)

Libraries
	•	requests
	•	pandas
	•	psycopg2
	•	sqlalchemy

Database
	•	PostgreSQL 15

Dashboard
	•	Tableau Public / Desktop

🚀 Features

✔ Real-time Weather & AQI Fetching (5-minute intervals)

Uses API calls to collect live data of multiple Indian cities.

✔ Automated Raw Data Storage

Every API response is saved as a JSON file for reproducibility.

✔ PostgreSQL Data Warehouse

Two tables:
	weather_data
	aqi_data
✔ Data Cleaning & EDA

Performed using Python + SQL:
	•	Missing value check
	•	Outliers
	•	Dominant pollutant identification
	•	Max/Min/Avg temperature & AQI
	•	Trend analysis
✔ Tableau Dashboard

A clean interactive dashboard with:
	•	Top cities with highest temperature
	•	Highest humidity regions
	•	AQI comparison across cities
	•	Trend over time
📡 How the Pipeline Works

1️⃣ Fetch Data

fetch_apis.py pulls weather + AQI data every 5 min.

2️⃣ Store Raw Data

JSON dumped in /data/raw/.

3️⃣ Insert into PostgreSQL

store_data.py writes cleaned rows into the database.

4️⃣ Clean & Analyze Data

analyze_data.py generates clean CSVs in /data/clean/.

5️⃣ Build Dashboard in Tableau

Connect to clean CSVs and create visuals.

📊 Dashboard Highlights
	•	🔥 Highest Temperature Cities
	•	💧 High Humidity Alerts
	•	🏭 Most Polluted Cities
	•	📈 Weather & AQI Trend Over 24 Hours

Tabluea dashboard link:
https://public.tableau.com/views/Weatherandairqualityanalysis/Dashboard1?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link
