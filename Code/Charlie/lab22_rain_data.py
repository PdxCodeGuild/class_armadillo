import requests
from datetime import datetime
import re
import json
# date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')



url = 'https://or.water.usgs.gov/non-usgs/bes/multnomah.rain'

response = requests.get(url)

multnomah_rain = json.loads(response.text)

# Use regular expression to identify the date and total amount of rain fall
def day_in_month(multnomah_rain):
    pattern = (r'\d+-\w+-\d+\s+(\d+)', multnomah_rain)
    monthly_rain = findall(pattern, multnomah_rain)
    return monthly_rain
 


 # call our function
day_in_month = day_in_month(multnomah_rain
# create an empty dictionary to hold our data
daa = {}
# iterate over the touples in dates
for date in day_in_month:
    # make the touple a list
    day_in_month = list(day_in_month)
    
    day_in_month[0] = datetime.datetime.strptime(day_in_month[0], '%d-%b-%Y')
    # make our rainfall value into an integer
    day_in_month[1] = int(day_in_month[1])
    # add to dictionary with date as a key, and the integer as value
    data.update({day_in_month[0]: day_in_month[1]})




# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00
# print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016