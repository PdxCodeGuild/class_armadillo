# from module import CLASS
from datetime import datetime
import requests
import re

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
  average = get_mean(rain_data)
  total = 0
  for num in rain_data:
    total += (rain_data - mean) ** 2
    return total / len(rain_data)

def variance(nums):
    average = mean(nums)
    total = 0
    for num in nums:
        total += (num - average) ** 2
    return total / len(nums)

# https://en.wikipedia.org/wiki/Standard_deviation
def standard_deviation(nums):
    return math.sqrt(variance(nums))

nums = [random.randint(1, 99) for _ in range(100)]
print(f'The mean is {mean(nums)}')
print(f'The variance is {variance(nums)}')
print(f'The standard deviation is {standard_deviation(nums)}')


date = get_rain(text) # calls function