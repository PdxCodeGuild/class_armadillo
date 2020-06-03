from datetime import date
import requests
import re

def get_data(url):
   website_data = requests.get(url)
   weather_table = website_data.text
   date_tuples = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', weather_table)
   return date_tuples



def timedate():
   today = date.today()
   # print(today.year)
   # print(today.month)
   # print(today.day)
   # print(today)
   # print(today.strftime('%d-%b-%Y'))
   return today.strftime('%d-%b-%Y')

timedate = timedate()

print(timedate)

weather_tuples = get_data('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')

print(weather_tuples)

# from datetime import datetime
# ​
# text = '''
# Hayden Island Rain Gage - 1740 N. Jantzen Beach Ctr.
# ​
# PROVISIONAL, UNCORRECTED RAW DATA FROM THE CITY OF PORTLAND HYDRA NETWORK.
# Data are the number of tips of the rain gage bucket.
# Each tip is 0.01 inches of rainfall.
#  [-, missing data]
# Dates and times are PACIFIC STANDARD TIME.
# ​
#             Daily  Hourly data -->
#    Date     Total    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
# ------------------------------------------------------------------------------------------------------------------
# 01-MAY-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0
# 30-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 29-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 28-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 27-APR-2020     3    0   2   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 26-APR-2020     5    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   2   3   0
# 25-APR-2020    16    0   0   0   0   0   0   5   8   2   0   0   0   0   0   0   1   0   0   0   0   0   0   0   0
# 24-APR-2020     2    0   0   0   0   0   0   0   0   1   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 23-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 22-APR-2020    23    0   0   0   0   2   4   0   3   6   3   0   4   0   0   1   0   0   0   0   0   0   0   0   0
# 21-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 20-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 19-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 18-APR-2020    18    0   0   0   0   0   0   0   0   1   1   1   2   0   0   1   1   0   4   6   0   0   0   0   1
# 17-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 16-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 15-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# '''
# ​
# ​
# ​
# ​
# # represent data as a list of dictionaries, with a tuple for the date
# data = [{
#     'date': (2020, 5, 1),
#     'total': 0
# },{
#     'date': (2020, 4, 30),
#     'total': 0
# },
# ...
# {
#     'date': (2020, 4, 25),
#     'total': 16
# }]
# ​
# # represent data as a list of tuples with datetime objects
# data = [
#     (datetime(2020, 5, 1), 0),
#     (datetime(2020, 4, 30), 0)
# ]
# ​
# # represent the data as a list of instances of DailyRain
# class DailyRain:
#     def __init__(self, date, total):
#         self.date = date
#         self.total = total


'''
Lab 22: Rain Data
The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland, and publishes their data publicly: http://or.water.usgs.gov/non-usgs/bes/

The data tables available on the site look something like...

Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...

Download one of these files and write a function to load the file. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries, or a list of instances of a custom class.

To parse the dates, use datetime.strptime. This allows for easy access to the year, month, and day as ints. Below I've shown how to parse an example string, resulting in a datetime object. We can then access the year, month, and day on that datetime as ints. Later, if you want to print the datetime in a more human-readable format, you can use datetime.strftime.

import datetime
date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
print(date.year)   # 2016
print(date.month)  # 3
print(date.day)    # 25
print(date)  # 2016-03-25 00:00:00
print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016
Version 2
Now that you've successfully extracted the data, let's done some statistics.

1. Calculate the mean of the data:
mean

2. Use the mean to calculate the standard deviation, which is a measure of how "spread out" the data is:
standard_deviation

68.2% of the data falls within 1 standard deviation of the mean.

bell_curve

3. Find the day which had the most rain.
4. Find the year which had the most rain on average.
Version 3
Using matplotlib create a chart of the dates and the daily totals for a given year. The x_values will be a list of dates, The y_values are a list of the daily totals. If you don't have matplotlib installed, run pip install matplotlib. You can learn more about matplotlib here.

import matplotlib.pyplot as plt
...
plt.plot(x_values, y_values)
plt.show()
Some charts you can make are:

all the data, date vs daily total
monthly totals, average across multiple years
total yearly rainfall, year by year
Version 4 (optional)
Use regular expressions to pull all the .rain files from the html source of the main page and do statistics on all of them.
'''