# version 2

from datetime import datetime
import re 
import requests


# define the path and open text file

# gets data from website
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/metro_center.rain') # gets data from website
text = response.text #turns into text format

def rain_data(text): # function 
    return re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text) # regular expression we want to find EVERYTHING that fits this criteria
        # \d means digits
        # \w means words
        # \s means space
        # () means capture groups - we are splitting it into these groups

dates = rain_data(text) # calls above function
rain_list = [] # empty list for collecting formatted date tuples from below loop
for date in dates: # iterates through each tuples (date) of the 'dates' list
    rain = (datetime.strptime(date[0], '%d-%b-%Y')), int(date[1]) # transforms date in each tuple to date objects
    print(rain)  # (datetime.datetime(2002, 5, 23, 0, 0), 0)]

    rain_list.append(rain) # adds date formatted tuples to list

print(rain_list)
# Rainlist

# (2002, 10, 18, 0, 0), 0), (datetime.datetime(2002, 10, 17, 0, 0), 0), (datetime.datetime(2002, 10, 16, 0, 0), 0), (datetime.datetime(2002, 10, 15, 0, 0), 0), (datetime.datetime(2002, 10, 14, 0, 0), 0), 
# (datetime.datetime(2002, 10, 13, 0, 0), 0), (datetime.datetime(2002, 10, 12, 0, 0), 0), (datetime.datetime(2002, 10, 11, 0, 0), 0), (datetime.datetime(2002, 10, 10, 0, 0), 0), (datetime.datetime(2002, 10, 9, 0, 0), 0), (datetime.datetime(2002, 10, 8, 0, 0), 0), (datetime.datetime(2002, 10, 7, 0, 0), 0), (datetime.datetime(2002, 10
def get_mean(rain_list):  # creating a function
  total = 0   #current sum set to zero so we can add to it
  for water in rain_list: # for loop, each element will be called water
    total += water[1]
    # I am accessing the water list from above
    # total = total + water 
    
  return total/len(rain_data) # average == total sum / how many









# Calculae the Mean
# The mean is the sum of all the daily totals divided by the 
# number of daily totals.



