-- Create a table to store weather data
CREATE TABLE IF NOT EXISTS weather_data (
    Sl_no SERIAL PRIMARY KEY,
    city VARCHAR(50),
    temperature FLOAT,
    humidity INT,
    condition VARCHAR(100),
    wind_speed FLOAT,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Create a table to store aqi data
CREATE TABLE IF NOT EXISTS aqi_data (
    Sl_no SERIAL PRIMARY KEY,
    city VARCHAR(50),
    aqi INT,
    dominent_pollutant VARCHAR(50),
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

SELECT * FROM weather_data;
SELECT * FROM aqi_data;

