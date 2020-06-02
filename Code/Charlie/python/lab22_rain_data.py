from datetime import datetime
import requests
import re
import math

def load_rain_data(url):
    data = requests.get(url)
    text = data.text
    rain_data = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text)
    


    for i in range(len(rain_data)):
        date = rain_data[i][0]
        daily_total = rain_data[i][1]
        daily_total = int(daily_total)*0.01 * 2.54
        
        rain_data[i] = {
            'date': date,
            'daily_total' : daily_total,
        }
    return rain_data

  

def calc_mean(rain_data):

    total = 0
    for row in rain_data:
        total += row['daily_total']
    return total / len(rain_data)

def calc_var(rain_data, mean):
    total = 0
    for row in rain_data:
        total += (row['daily_total'] - mean ) **2
    return total / len(rain_data)

def highest(rain_data):
    highest_rain = rain_data[0]
    for row in rain_data:
        if row['daily_total'] > highest_rain['daily_total']:
            highest_rain = row
    return highest_rain


rain_data = load_rain_data('https://or.water.usgs.gov/non-usgs/bes/yeon.rain')
mean = calc_mean(rain_data)
variance = calc_var(rain_data, mean)
stan_dev = math.sqrt(variance)
highest_rain = highest(rain_data)


print(f'\nThe mean of this rain data is {mean}')
print(f'\n68% of the data falls in a range greater than {mean-stan_dev} and less than {mean+stan_dev}')
print(f'\nThe day with the most rain was {highest_rain["date"]} with {highest_rain["daily_total"]} cm. \n')
