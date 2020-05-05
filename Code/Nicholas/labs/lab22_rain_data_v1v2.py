# In lab 22 we take daily rain data from a list of reported measure in PDX and use 
# list methods and regular expressions to make it more useable for statistical operations.  
# We then carried out basic statistical methods on the data

# Eco Roof Rain Gage - SW 12th and Clay

# PROVISIONAL, UNCORRECTED RAW DATA FROM THE CITY OF PORTLAND HYDRA NETWORK.
# Data are the number of tips of the rain gage bucket.
# Each tip is 0.01 inches of rainfall.
#  [-, missing data]
# Dates and times are PACIFIC STANDARD TIME.
from datetime import datetime # import datetime
import re # import regular expressions
import requests
import math #import math for variance

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/twelfth_and_clay.rain')
text = response.text


rain_data = re.findall(r"(\d+\D\w+\D\d+)\s+(\d+)", text)  # use regular expressions to parse out the req'd first two columns
# print(rain_data)
for i in range(len(rain_data)):  #iterates over generated list of rain data
    date = rain_data[i][0]  #assigns first index as date 
    daily_rain = rain_data[i][1]  #assigns second index as rain
    date = datetime.strptime(date, '%d-%b-%Y')  # uses datetime.strptime to make each part of date accessible
    rain_data[i] = (date, daily_rain)  #makes date and daily rain into tuple
    # print(rain_data[i]) #prints tuples

# version 2
total = 0 # start with zero total 
for i in range(len(daily_rain)): #iterate over daily rain list
    total += int(rain_data[i][1])  #add all daily rain totals(convert list to int)
    mean = total / len(daily_rain)   #divide daily rain totals by total days for mean
print(f'The mean rainfall is {mean}.')    
  

  
total = 0
for i in range(len(daily_rain)):  # iterate over daily rain totals
    total += (int(rain_data[i][1]) - mean) ** 2  #add all daily rain totals, subtract mean, square
    variance = total / len(daily_rain)  #totals/days
print(f'The variance is {variance}.')    

standard_deviation = math.sqrt(variance) #sd = variance squared
print(f'The standard deviation is {standard_deviation}.')

