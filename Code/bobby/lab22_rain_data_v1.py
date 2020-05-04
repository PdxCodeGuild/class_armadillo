

import requests
import re
from datetime import datetime

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/walmart_ecoroof.rain') # gets data from website
text = response.text # turns into text format

pir_rain_gauge = re.findall(r"(\d+-\w+-\d+) \s+ (\d+)", text)
   
for i in range(len(pir_rain_gauge)):
    date = pir_rain_gauge[i][0]
    daily_tot = pir_rain_gauge [i][1]
    date = datetime.strptime(date, "%d-%b-%Y")

    daily_tot = int(daily_tot)*0.01*2.54

pir_rain_gauge[i] = {
    "date": date,
    "daily_tot": daily_tot
}

x = []
y = []

for row in pir_rain_gauge:
    if row ['date'].year == 2010 and row ['date'].month == 3:
        x.append(row['date'])
        y.append(row['daily_tot'])


