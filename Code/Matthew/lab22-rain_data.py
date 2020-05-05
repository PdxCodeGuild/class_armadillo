
import re
import requests
from datetime import datetime
import matplotlib.pyplot as plt

# get the data from the website
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
text = response.text

# pull out the dates and daily totals
data = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text)
# print(data)

# loop over the data
for i in range(len(data)):
    date = data[i][0] # get the date
    daily_total = data[i][1] # get the daily total
    date = datetime.strptime(date, '%d-%b-%Y') # convert the string date into a datetime object

    daily_total = int(daily_total)*0.01*2.54 # convert tips to centimeters

    # make the record a tuple or dictionary
    # data[i] = (date, daily_total)
    data[i] = {
        'date': date,
        'daily_total': daily_total
    }

# split our data into x and y values
x_values = []
y_values = []
for row in data:
    if row['date'].year == 2010 and row['date'].month == 3:
        x_values.append(row['date'])
        y_values.append(row['daily_total'])

# make a fancy chart
plt.plot(x_values, y_values)
plt.show()

