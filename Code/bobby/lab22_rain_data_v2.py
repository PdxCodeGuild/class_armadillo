import requests
import re
from datetime import datetime
import matplotlib.pyplot as plt

# Pulling the data fromt the website.
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/walmart_ecoroof.rain') # gets data from website
# turns into text format
text = response.text

# Getting the data for each date and the daily total
pir_rain_gauge = re.findall(r"(\d+-\w+-\d+) \s+ (\d+)", text)
print(pir_rain_gauge)
   
# Using a for loop to go over that data
for i in range (len(pir_rain_gauge)):
    # Pulls the date
    date = pir_rain_gauge[i][0]
    # Gets the daily total
    daily = pir_rain_gauge [i][1]
    # This is to convert the date str into a datetime obj
    date = datetime.strptime(date, "%d-%b-%Y")
    # Changes into centimeters
    daily = int(daily)*0.01*2.54
# This is suppose to make a tuple for the date and daily total.
    pir_rain_gauge[i] = {
        "date": date,
        "daily": daily
}
# splits the data into x and y values
x = []
y = []
for row in pir_rain_gauge:
    if row["date"].year == 2019 and row["date"].month == 12:
        x.append(row["date"])
        y.append(row["daily"])

# This to make a chart of the data
plt.plot(x, y)
plt.show()