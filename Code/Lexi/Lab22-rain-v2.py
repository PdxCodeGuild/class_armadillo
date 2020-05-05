# from module import CLASS
from datetime import datetime
import requests
import re
import math

#https://www.w3schools.com/python/ref_requests_response.asp
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
text = response.text

def get_rain(text): # create function
    return re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text)
 
def get_data(dates):
  # create empty list to fill
  rain_data = []
  # iterate through list
  for day in date: 
      # use special format for list
      rain = datetime.strptime(day[0], '%d-%b-%Y'), int(day[1])
      # adds date to empty list we created
      rain_data.append(rain) 
      # return list
  return rain_data

def get_mean(rain_data):
  # start with 0
  total = 0
  # iterate through list
  for height in rain_data:
    # add to total
    total += height[1]
    # get the avg
  return total / len(rain_data) 

#The standard deviation is the square root of the variance. 
# 68.2% of the data falls within 1 standard deviation of 
# the mean.

def get_variance(rain_data):
  total = 0
  for height in rain_data:
    total += (height[1] - get_mean(rain_data)) ** 2
    return total / len(rain_data)


# https://en.wikipedia.org/wiki/Standard_deviation
def standard_deviation(nums):
    return math.sqrt(get_variance(rain_data))


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
   date = get_rain(text)
   rain_data = get_data(day)
   mean = get_mean(rain_data)
   variance = get_variance(rain_data)
   standard_deviation = get_stand_dev(rain_data)
   max_rain_day = get_max_day(rain_data)

   print(f'Mean: {mean} tips')
   print(f'Variance: {variance}')
   print(f'Standard deviation: {standard_deviation}')
   print(f'Wettest day:{max_rain_day}')


rain_numbers() # calls above function


