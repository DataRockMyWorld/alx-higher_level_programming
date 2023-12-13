-- Top 3 cities during July & August by Temp

SELECT city, AVG(value) AS avg_temp 
FROM temperatures WHERE month IN (7, 8) AND value IS NOT NULL
GROUP BY city 
ORDER BY avg_temp DESC 
LIMIT 3;