import requests
from datetime import datetime
import re
import math


url = requests.get('https://or.water.usgs.gov/non-usgs/bes/wilson.rain')

wilson_rainfall = url.text


monthly_rainfall = re.findall('(\d+-\w+-\d+)(\s+\d+)', wilson_rainfall)


date_list = []
rainfall_list = []
for date,rainfall in monthly_rainfall:
    date_list.append(date)
    rainfall_list.append(rainfall)

rainfall_list = [num.strip(' ') for num in rainfall_list] # list comprehension strips whitespace from rainfall list
rainfall_list = [int(num) for num in rainfall_list] # converts string digits to integers
date_digits = []
for date in date_list:
    date = datetime.strptime(date, '%d-%b-%Y')
    date_digits.append(date)

clean_dates = []
for tup in date_digits:
    date_tuple = (tup.year, tup.month, tup.day)
    clean_dates.append(date_tuple)



rainfall_dictionary = dict(zip(clean_dates,rainfall_list))


# Calculate the Mean
# The mean is the sum of all the daily totals divided by the number of daily totals.
mean = sum(rainfall_list) / len(rainfall_list)


# Calculate the Variance
# Use the mean to calculate the variance, which is a measure of how "spread out" the data is:
variance_list = []
for num in rainfall_list:
    num -= mean    # Subtract the mean from each data point.
    num *= num     # Square each result.
    variance_list.append(num)
variance = sum(variance_list) / (len(variance_list) - 1) # Find the sum of the squared values. Divide by n - 1, where n is the number of data points.
standard_deviation = math.sqrt(variance)# The standard deviation is the square root of the variance. 68.2% of the data falls within 1 standard deviation of the mean.

# Loop over all the records to find the one which had the most rain, print out the date and daily total to the user.
inverse = [(rainfall, date) for date, rainfall in rainfall_dictionary.items()]
most_rain_date = (max(inverse)[1])


print(f'The most rain for the Wilson area fell on {most_rain_date} which was {rainfall_dictionary[most_rain_date]} tips')





