SELECT * FROM aqi_data;

-- Total number of rows
SELECT city,COUNT(*) FROM aqi_data
GROUP BY city;

-- CHECK FOR NULL VALUES
SELECT * FROM aqi_data
WHERE city IS NULL
	OR aqi IS NULL
	OR dominent_pollutant IS NULL
	OR 'condition' IS NULL
	OR timestamp IS NULL
;

-- DETECT OUTLIERS
SELECT * FROM weather_data
WHERE aqi < 0
	OR aqi > 500
	OR dominent_pollutant < 0
	OR dominent_pollutant > 1000
;

-- CHECK FOR MIN, MAX, AVG temperature and humidity
SELECT city,
	ROUND(AVG(aqi),2) AS avg_aqi,
	MAX(aqi) AS max_aqi,
	MIN(aqi) AS min_aqi
FROM aqi_data
GROUP BY city
;



