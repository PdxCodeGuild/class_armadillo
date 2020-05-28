
import math
import re
import requests
from datetime import datetime
#import matplotlib.pyplot as plt


def load_data(url):

    # get the data from the website
    response = requests.get(url)
    text = response.text

    # pull out the dates and daily totals
    data = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text)
    # print(data)

    # loop over the data
    for i in range(len(data)):
        date = data[i][0] # get the date
        daily_total = data[i][1] # get the daily total
        date = datetime.strptime(date, '%d-%b-%Y') # convert the string date into a datetime object

        daily_total = int(daily_total)*0.01*2.54 # convert tips to centimeters

        # make the record a tuple or dictionary
        # data[i] = (date, daily_total)
        data[i] = {
            'date': date,
            'daily_total': daily_total
        }

    # print(data[0:20])
    return data

def calculate_mean(data):
    total = 0
    for row in data: # iterate over our list of dictionaries
        total += row['daily_total'] # add the dictionary's daily total to the running sum
    return total / len(data)

def calculate_variance(data, mean):
    total = 0
    for row in data:
        total += (row['daily_total'] - mean) ** 2
    return total / len(data)

def most_rain(data):
    row_most_rain = data[0] # running maximum
    for row in data:
        # if the current dictionary's daily total is greater than the daily total of our running maximum
        # assign the running maximum to the current dictionary
        if row['daily_total'] > row_most_rain['daily_total']:
            row_most_rain = row
    return row_most_rain


data = load_data('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
# data = load_data('https://or.water.usgs.gov/non-usgs/bes/open_meadows.rain')

print('starting date:', data[len(data)-1]['date'])
print('ending date:', data[0]['date'])
print('number of records:', len(data))
mean = calculate_mean(data)
print('mean:', mean, 'cm')
variance = calculate_variance(data, mean)
print('variance:', variance, 'cm^2')
standard_deviation = math.sqrt(variance)
print('standard deviation:', standard_deviation, 'cm')
print(f'this means that 68% of the data falls within {mean-standard_deviation} cm and {mean+standard_deviation} cm')
row_most_rain = most_rain(data)
print(f'the day with the most rain was {row_most_rain["date"]} with {row_most_rain["daily_total"]} cm')

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

