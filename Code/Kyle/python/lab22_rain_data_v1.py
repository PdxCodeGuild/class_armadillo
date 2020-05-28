# Lab 22 Rain Data Version 1
# Kyle Harasimowicz


import re 
import requests
import string
from datetime import datetime

# Pull data
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/metro_center.rain') 
text = response.text


dates = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text)
list_rainfall = [] 
for date in dates: 
    rain = (datetime.strptime(date[0], '%d-%b-%Y')), int(date[1]) 
    print(rain)
    list_rainfall.append(rain) 

print(list_rainfall)