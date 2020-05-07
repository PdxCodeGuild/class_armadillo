import datetime
import requests
import re
import random
import math
from datetime import datetime

# Url method of grabbing data

# url = ('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')

# request_data = requests.get(url)
# text = request_data.text

# Text file method of grabbing data

filename = 'Code\Lawrence_House\hayden_island.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

# Regular expression for finding date and total rainfall

regex = r"(\d+-\w+-\d+)\s+(\d+)"
match = re.findall(regex, text)
# print(match)

for i in range(len(match)):
    date = match[i][0] #get date
    daily_total = match[i][1] #get daily total
    date = datetime.strptime(date, '%d-%b-%Y')

    daily_total = int(daily_total)*0.01*2.54
    match[i]= {
        'date': date,
        'daily_total': daily_total
    }

def mean(match):
    total = 0
    for line in match:
        total += line['daily_total']
    return total / len(match)

print('This is the mean: ', mean(match))

def variance(match):
    average = mean(match)
    total = 0
    for line in match:
        total += (line['daily_total'] - average) ** 2
    return total / len(match)

print(f'The variance is {variance(match)}')

def standard_deviation(match):
    return math.sqrt(variance(match))

print(f'The standard deviation is {standard_deviation(match)}')

# print(max(mean))

# x_values = []
# y_values = []
# for row in match:
#     if row['date'].year == 2010 and row['date'].month == 3:
#         x_values.append
