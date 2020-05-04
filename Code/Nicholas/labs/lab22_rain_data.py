# Eco Roof Rain Gage - SW 12th and Clay

# PROVISIONAL, UNCORRECTED RAW DATA FROM THE CITY OF PORTLAND HYDRA NETWORK.
# Data are the number of tips of the rain gage bucket.
# Each tip is 0.01 inches of rainfall.
#  [-, missing data]
# Dates and times are PACIFIC STANDARD TIME.
from datetime import datetime 
import re
import requests

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

# def mean(daily_rain):
#     total = 1
#     for day in daily_rain:
#         total += rain_data
#         return total / len(daily_rain)   
  