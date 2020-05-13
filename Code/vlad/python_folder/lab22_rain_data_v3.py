# Lab22 Rain Data Version 3 is optional https://github.com/PdxCodeGuild/class_armadillo/blob/master/1%20Python/labs/lab22-rain_data.md

"""Version 3
Using matplotlib create a chart of the dates and the daily totals for a given year. The x_values will be a list of dates, The y_values are a list of the daily totals. If you don't have matplotlib installed, run pip install matplotlib. You can learn more about matplotlib here.

import matplotlib.pyplot as plt
...
plt.plot(x_values, y_values)
plt.show()
Some charts you can make are:

all the data, date vs daily total
monthly totals, average across multiple years
total yearly rainfall, year by year"""

#to get the graph for the matplotlib library 
""" Installed pip3 install matplotlib """

# then use the following list to get the x and y axes 
# I need to make it into the datetime format so the graph charts get good graphs: 

import string
import requests
import re
import math
import datetime
import random
import statistics 
from datetime import datetime
import matplotlib.pyplot as plt

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
rain_data = response.text

# find all the matching phone numbers
date_and_daily_total = r'(\d+-\w+-\d+)\s+(\d+)' # expression 
results = re.findall(date_and_daily_total, rain_data) # this is making a list of Tuples

# use the starter code from the lab22 to make it it string dates to be intergers to be  
# from datetime import datetime # I have this like at the time comment here so it does not repeat

# use a for loop to go to each of the dates and change into change it into numbers into an interger and to change from tuple to a list
rain_data_dict = {} # use this empty dictionry
for rain in results:
   rain = list(rain) # this will change from tuple to a list because Tuples can't be edited or change values 
   # print(type(rain))
# turn a string into a datetime object
   rain[0] = datetime.strptime(rain[0], '%d-%b-%Y') # this is to get to the first element of the list #if using the from datetime import datetime only need to sue one datetime instead of datetime.time
   rain[1] = int(rain[1]) # turning string into interger to change the second value from a string to an interger to add it later
   rain_data_dict.update({rain[0]:rain[1]}) # the key is the  date and the value is how much rain has fallen 
# print(rain_data_dict)

# I need to make my datetime object  subcriptable 

# access the properties of that object
#print(type(rain_data_dict[0].year))   # LEArn how to use this print version
# print(rain_data.month)  # 3
# print(rain_data.day)    # 25
# print(rain_data)  # 2016-03-25 00:00:00

# turn the datetime object back into a string
# print(rain_data.strftime('%d-%b-%Y'))  # 25-Mar-2016

# # I need to make the daily total to be an interger so I can take the average of them 
# also I need to clean the data ask what else do I need to do to clean this data

# import random
# import math



""" use the following functions below to get version number 2 mean, variance and 
standard_deviation """

#function to get the mean: 
# https://en.wikipedia.org/wiki/Arithmetic_mean

def mean(rain_data_dict):
   total = 0
   for key, value in rain_data_dict.items(): # we need this logic to get inside the key or value pair in a dictionary 
      # print(value)
      total += value
   return total / len(rain_data_dict) # get inside the dictionary to get the value of the years

average = mean(rain_data_dict)
print(average) # 9.604221969409682


# function to get the Variance: 
# https://en.wikipedia.org/wiki/Variance

def variance(rain_data_dict, average):
   #  average = mean(rain_data_dict) I do not need this because I passed as a argument from the mean function above
   total = 0
   for key, value in rain_data_dict.items():
      total += (value - average) ** 2
   return total / len(rain_data_dict)

variances = variance(rain_data_dict, average)
print(variances) # 481.5039589162603


# function to get the standard_deviation: 
# https://en.wikipedia.org/wiki/Standard_deviation

def standard_deviation(variances):
   return math.sqrt(variances)
deviations = standard_deviation(variances)

# nums = [random.randint(1, 99) for _ in range(100)]
# print(f'The mean is {average}') # 9.604221969409682
# print(f'The variance is {variances}') #481.5039589162603
# print(f'The standard deviation is {deviations}') #21.943198465954325




# split our data into x and y values
x_values = []
y_values = []

print('please enter a valid year and  betweek 1998 and 2020 how much rain has fallen in a Portland Address at Hayden Island: ')

while True:
     
    # input validation put it in a loop for the month 1-12 and year 
    # taking year as a string: 
    year = (input('Please enter the year to see a graph showing how much rain has fallen for that whole year: '))
    # changing the string year user input and turning into a int: 
    if year.isdigit():
        year = int(year)
        if year > 1997 and year < 2021:
            break

    else:
        print('Please enter a 4 digit number for the year between 1997 and 2020: ')

while True:
    month = (input('Please enter the month to see a graph showing how much rain has fallen for that whole month: '))
    if month.isdigit():
        month = int(month)
        if month > 0 and month < 13:
            break
    else:
        print('Please enter a 2 digit number for the month month 1-12: ')
    
# to check for multiple years 
for day in rain_data_dict:
    # print(day.year)
    if day.year == year and day.month == month: # check for all the months and year user enter according to user Input: 
    
    # print(day)

        x_values.append(day)  
        y_values.append(rain_data_dict[day])

# make a fancy chart
plt.plot(x_values, y_values)
plt.show()
    
# =======================================================================================

# Starter code by the instructor: 

# import re
# import requests
# from datetime import datetime
# import matplotlib.pyplot as plt

# # get the data from the website
# response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
# text = response.text

# # pull out the dates and daily totals
# data = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text)
# # print(data)

# # loop over the data
# for i in range(len(data)):
#     date = data[i][0] # get the date
#     daily_total = data[i][1] # get the daily total
#     date = datetime.strptime(date, '%d-%b-%Y') # convert the string date into a datetime object

#     daily_total = int(daily_total)*0.01*2.54 # convert tips to centimeters

#     # make the record a tuple or dictionary
#     # data[i] = (date, daily_total)
#     data[i] = {
#         'date': date,
#         'daily_total': daily_total
#     }

# # split our data into x and y values
# x_values = []
# y_values = []
# for row in data:
#     if row['date'].year == 2010 and row['date'].month == 3:
#         x_values.append(row['date'])
#         y_values.append(row['daily_total'])

# # make a fancy chart
# plt.plot(x_values, y_values)
# plt.show()
