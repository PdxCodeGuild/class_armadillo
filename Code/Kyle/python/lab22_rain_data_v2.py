# Lab 22 Rain Data Version 2
# Kyle Harasimowicz

import requests
import math
import re
import string
from datetime import datetime

# Pull data
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/metro_center.rain') 
text = response.text


dates = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text)
list_rainfall = [] 
for date in dates:
    rain_data = (datetime.strptime(date[0], '%d-%b-%Y')), int(date[1]) 
    print(rain_data)
    list_rainfall.append(rain_data)
    print(list_rainfall)


def mean(list_rainfall):
    sum = 0
    for r in list_rainfall:
        sum += r[1]
        mean = sum/len(list_rainfall)
        print(f'Mean: {mean}')
        return mean
        
def variance(list_rainfall):
    sum = 0
    for r in list_rainfall:
        sum += (r[1] - mean(list_rainfall)) **2
        variance = sum / len(list_rainfall)
        print(f'Variance: {variance}')
        return variance

def standard_deviation(list_rainfall):
    sd = math.sqrt(variance(list_rainfall))
    print(f'Standard Deviation: {sd}')
    return sd

mean(list_rainfall)
variance(list_rainfall)
standard_deviation(list_rainfall)