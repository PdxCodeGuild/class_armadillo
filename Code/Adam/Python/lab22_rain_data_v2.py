"""
Lab 22: Rain Data

The 'City of Portland Bureau of Environmental Services' operates and maintains 
a network of rain gauges around Portland, and publishes their data publicly: 
http://or.water.usgs.gov/non-usgs/bes/

The data tables available on the site look something like...

Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...

Version 1
Download or use requests to get these files. The two columns that are most 
important are the date and the daily total. The simplest representation of this
data is a list of tuples, but you may also use a list of dictionaries, or a 
list of instances of a custom class.

To parse the dates, use datetime.strptime. This allows for easy access to the 
year, month, and day as ints. Below I've shown how to parse an example string, 
resulting in a datetime object. We can then access the year, month, and day on 
that datetime as ints. Later, if you want to print the datetime in a more 
human-readable format, you can use datetime.strftime.

Version 2

1. Calculae the Mean

2. Calculate the Variance

"""
from datetime import datetime
import math
import statistics
import requests
import re


print('Sylvania PCC Rain Gage') 

# sending a request to the url
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/pcc_sylvania.rain')
# assigning the reponse to the variable data
data = response.text
# print(data) # checking that response was recieved


# using regex to isolate the date pattern and first column of daily totals
date_n_dtotal = re.findall('(\d+-\w+-\d+)\s+(\d+)', data)
# print(date_n_dtotal)


# declaring seperate lists to store dates and daily_totals
dates = []
daily_totals = []


# data is a list of tuples; use the len() function to get the total number of 
# tuples in list and iterating over the range of that total
for i in range(len(date_n_dtotal)):
    # adding each date to a the list dates with the append function
    dates.append(date_n_dtotal[i][0])
    # adding each daily total to a the list daily_totals
    daily_totals.append(date_n_dtotal[i][1])


# convert each string in the list of strings to an integer for operations later
daily_totals = [int(i) for i in daily_totals]
# print(daily_totals)


# use the len() funtion to find the number of daily totals
num_of_dtotals = len(daily_totals)
# print(f'There are {num_of_dtotals} daily totals on record.')


# use the sum() function to find the sum of a list of numbers
sum_of_dtotals = sum(daily_totals)
# print(f'The sum of all the daily totals is {sum_of_dtotals}')


# calculate the mean by dividing the the sum of daily totals by the number of daily totals
# mean = sum_of_dtotals / num_of_dtotals
# print(mean)

# using the fmean function from the statistics module to calculate the mean
f_mean = statistics.fmean(daily_totals)
print(f'The mean of daily totals is: {round(f_mean, 2)}')


# use variance function to find he variance
dtotal_variance = statistics.variance(daily_totals, f_mean)
print(f'The daily totals have a variance of {round(dtotal_variance, 2)}')

#  the standard deviation is the variance squared
standard_deviation = math.sqrt(dtotal_variance)
print(f'The standard deviation is {round(standard_deviation, 2)}%')


# combine dates and daily_totals to make a dictionary
# then find the max of the dictionary
date_n_dtotal_dict = dict(zip(dates, daily_totals))
# print(date_n_dtotal_dict)

# use the max funtion to find the date with the highest value
most_rain_date = max(date_n_dtotal_dict, key=date_n_dtotal_dict.get)


# use the max funtion to find highest value
# multiple the hightwst value by .01 because each value is .01 inches of rainfall.
most_rain = max(date_n_dtotal_dict.values())*.01
print(f'The most daily rain occurred on {most_rain_date} when it rained {most_rain} inches.')

