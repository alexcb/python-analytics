#!/bin/sh
set -e
year=2000
while [ "$year" -lt "2021" ]; do
	echo $year
	year=$(( $year + 1))
	echo $year
    curl "https://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=51337&Year=${year}&Month=6&Day=1&time=&timeframe=2&submit=Download+Data" > victoria-weather-$year.csv
done
