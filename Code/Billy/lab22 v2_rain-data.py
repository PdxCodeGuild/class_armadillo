from datetime import datetime
import requests
import re
import math


# text = '''
# Metro Learning Center Rain Gage - 2033 NW. Glisan St.

# PROVISIONAL, UNCORRECTED RAW DATA FROM THE CITY OF PORTLAND HYDRA NETWORK.
# Data are the number of tips of the rain gage bucket.
# Each tip is 0.01 inches of rainfall.
#  [-, missing data]
# Dates and times are PACIFIC STANDARD TIME.

#             Daily  Hourly data -->
#    Date     Total    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
# ------------------------------------------------------------------------------------------------------------------
# 01-MAY-2020    33    0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 30-APR-2020     6    0   0   0   0   0   0   0   0   1   0   0   2   2   1   0   0   0   0   0   0   0   0   0   0
# 29-APR-2020     3    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1   1   0   1   0   0   0   0   0
# 28-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 27-APR-2020     2    1   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 26-APR-2020     6    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1   4   1
# 25-APR-2020    33    0   0   0   0   0   0   5  15   2   1   0   0  10   0   0   0   0   0   0   0   0   0   0   0
# 24-APR-2020     4    0   0   0   0   0   0   0   0   3   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 23-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 22-APR-2020    32    0   0   0   0   2   3   0   2   9   3   0   5   0   1   6   0   0   0   0   0   0   1   0   0
# 21-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 20-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 19-APR-2020     1    0   0   0   0   0   0   0   0   0   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0
# 18-APR-2020     7    0   0   0   0   0   0   0   1   0   1   2   2   0   0   0   1   0   0   0   0   0   0   0   0
# 17-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 16-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# '''

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/metro_center.rain') # gets data from website
text = response.text # turns into text format

def get_rain(text): # parses text to return only the first two columns (date and daily total)
   return re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text) # regular expression for parsing text into first 2 columns, returns dates
   

def get_data(dates): # function to obtain date formattted rain data with parsed data as input
   rain_data = [] # empty list for collecting formated date tuples from below loop
   for date in dates: # iterates through each tuple(date) of the 'dates' tuple list
      rain = (datetime.strptime(date[0], '%d-%b-%Y'), int(date[1])) # transforms date in each tuple to date object and daily total to int
      rain_data.append(rain) # adds date formattted tuples to list
   return rain_data  # input for calculating mean, variance, standard deviation and max rain day                                                                                           d 


def get_mean(rain_data): # function that calculates avg of daily totals using date formatted rain_data as input
   total = 0 # indicates total sum of daily totals 
   for water in rain_data: # each tuple in the list
      total += water[1] # its second index position gets added to total sum of daily totals
   return total / len(rain_data) # math to obtain the mean


def get_variance(rain_data): # function that computes variance, using rain data as input
   total = 0 # indicates total sum of each iteration 
   for water in rain_data: # each tuple in list subject to below math
      total += (water[1] - get_mean(rain_data)) ** 2 # variance math
   return total / len(rain_data) # final variance math                                                                                                                                                                                           


def get_stand_dev(rain_data): # uses rain_data to indirectly determine standard deviation
   return math.sqrt(get_variance(rain_data)) # square root of the variance = standard deviationdA


def get_max_day(rain_data): # finds the tuple(s) with the hightest daily total.
   max_rain_day = ' ' # collects highest rain days as strings                                                                              
   maximum = max(rain_data, key=lambda x:x[1]) # selects tuple that has the highest secomd index, returns tuple that containest largest dily total value
   # max() would usually base it on first index of tuple, lambda key parameter specifies that max() should use index [1] to determine max
   for i in range(len(rain_data)): # iterates through rain data tuples
      if rain_data[i][1] == maximum[1]: # if tuple daily total equals max, it will included as max
         rain_data[i]= ((rain_data[i][0]).strftime('%d-%b-%Y'), rain_data[i][1]) # converts that tuple to readable date format
         max_rain_day += str(rain_data[i]) # adds highest tuple to max_rain_day
         # max_rain_day.append(rain_data[i]) # if collected via list instead of string
   return max_rain_day


def rain_numbers(): # main function, combines above functions
   dates = get_rain(text)
   rain_data = get_data(dates)
   mean = get_mean(rain_data)
   variance = get_variance(rain_data)
   standard_deviation = get_stand_dev(rain_data)
   max_rain_day = get_max_day(rain_data)

   print(f'Mean: {mean} tips')
   print(f'Variance: {variance}')
   print(f'Standard deviation: {standard_deviation}')
   print(f'Wettest day:{max_rain_day}')


rain_numbers() # calls above function








'''
# Lab 22: Rain Data


The 'City of Portland Bureau of Environmental Services' operates and maintains a network of rain gauges around Portland, and publishes their data publicly:  http://or.water.usgs.gov/non-usgs/bes/

The data tables available on the site look something like...

```
Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...

```

## Version 1

Download or use `requests` to get these files. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries, or a list of instances of a custom class.

To parse the dates, use [datetime.strptime](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior). This allows for easy access to the year, month, and day as `int`s. Below I've shown how to parse an example string, resulting in a [datetime](https://docs.python.org/3.6/library/datetime.html#date-objects) object. We can then access the year, month, and day on that datetime as ints. Later, if you want to print the datetime in a more human-readable format, you can use [datetime.strftime](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior).

```python
from datetime import datetime

# turn a string into a datetime object
date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')

# access the properties of that object
print(date.year)   # 2016
print(date.month)  # 3
print(date.day)    # 25
print(date)  # 2016-03-25 00:00:00

# turn the datetime object back into a string
print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016
```

## Version 2

Now that you've successfully extracted the data, let's calculate some statistics.

### 1. Calculae the Mean

The mean is the sum of all the daily totals divided by the number of daily totals.

![mean](images/average.png)


### 2. Calculate the Variance

Use the mean to calculate the variance, which is a measure of how "spread out" the data is:

![standard_deviation](images/variance.png)

The standard deviation is the square root of the variance. 68.2% of the data falls within 1 standard deviation of the mean.

![bell_curve](https://upload.wikimedia.org/wikipedia/commons/thumb/8/8c/Standard_deviation_diagram.svg/500px-Standard_deviation_diagram.svg.png)

### 3. Find the day which had the most rain.

Loop over all the records to find the one which had the most rain, print out the date and daily total to the user.
'''