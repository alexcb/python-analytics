import csv
import re
import os
import datetime
import matplotlib.pyplot as plt

script_dir = os.path.dirname(os.path.realpath(__file__))

def get_float_or_zero(s):
    if s == '':
        return 0.0
    return float(s)

def get_data():
    p = re.compile('victoria-weather-[0-9]+.csv')
    rows = []
    for filename in os.listdir(script_dir):
        if p.match(filename):
            path = os.path.join(script_dir, filename)
            with open(path, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
                for i, row in enumerate(spamreader):
                    if i == 0:
                        continue
                    rain_mm = get_float_or_zero(row[19])
                    snow_mm = get_float_or_zero(row[21])
                    year = int(row[5])
                    month = int(row[6])
                    day = int(row[7])
                    date = datetime.date(year, month, day)
                    rows.append([date, rain_mm, snow_mm])
    return rows

def get_yearly_cumsum(rows):
    year = None
    yearly_data = []
    cumsum_rows = []
    for date, rain, snow in rows:
        if year != date.year:
            if cumsum_rows:
                yearly_data.append([year, cumsum_rows])
            cumsum_rows = []
            cumrain = 0.0
            cumsnow = 0.0
            year = date.year
        cumrain += rain
        cumsnow += snow
        day_since_jan1 = get_days_since_jan1(date)
        cumsum_rows.append([day_since_jan1, cumrain, cumsnow])

    yearly_data.append([year, cumsum_rows])
    return yearly_data

def get_days_since_jan1(date):
    return date.timetuple().tm_yday - 1

def transpose(rows):
    dates = []
    rain = []
    snow = []
    for row in rows:
        dates.append(row[0])
        rain.append(row[1])
        snow.append(row[2])
    return dates, rain, snow


rows = get_data()

fig = plt.figure(figsize=(10.0, 10.0))
ax = fig.add_axes([0,0,1,1])

for year, data in get_yearly_cumsum(rows):
    day, rain, snow = transpose(data)
    percp = [x+y for x,y in zip(rain, snow)]
    ax.plot(day, percp, label=f'{year}')

ax.set_xlabel('days since jan 1st')
ax.set_ylabel('precipitation (mm)')
ax.set_title('Victoria BC cumulative yearly precipitation')
ax.legend()
fig.savefig('where-is-the-rain.png', bbox_inches='tight')
