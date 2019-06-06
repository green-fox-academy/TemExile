-- question 1
SELECT country_code FROM weather_station WHERE id = '724940:23234'

-- question 2
SELECT temperature FROM raw_weather_data 
    WHERE wsid = '724940:23234' and 
            month = 6 and 
            day = 1 and 
            year = 2008

-- question 3
SELECT temperature FROM raw_weather_data 
    WHERE wsid = '724940:23234' and 
            month = 6 and 
            day = 1 and 
            year = 2008 and 
            hour >= 9 and hour <=1

-- question 4

-- question 5
SELECT id, name, max(lat), state_code, country_code 
FROM weather_station WHERE state_code = 'TX' ALLOW FILTERING

