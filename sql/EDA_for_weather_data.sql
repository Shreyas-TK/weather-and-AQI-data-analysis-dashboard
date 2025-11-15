SELECT * FROM weather_data;

-- Total number of rows
SELECT city,COUNT(*) FROM weather_data
GROUP BY city;

-- CHECK FOR NULL VALUES
SELECT * FROM weather_data
WHERE city IS NULL
	OR temperature IS NULL
	OR humidity IS NULL
	OR 'condition' IS NULL
	OR wind_speed IS NULL
	OR timestamp IS NULL
;

-- DETECT OUTLIERS
SELECT * FROM weather_data
WHERE temperature < 0
	OR temperature > 50
	OR humidity < 0
	OR humidity > 100
;

-- CHECK FOR MIN, MAX, AVG temperature and humidity
SELECT city,
	ROUND(AVG(temperature)::numeric,2) AS avg_temp,
	MAX(temperature) AS max_temp,
	MIN(temperature) AS min_temp,
	ROUND(AVG(humidity):: numeric,2) AS avg_humidity,
	MAX(humidity) AS max_humidity,
	MIN(humidity) AS min_humidity
FROM weather_data
GROUP BY city;



