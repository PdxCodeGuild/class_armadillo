
#Download or use requests to get these files. The two columns that are most important are the date and the daily total. The simplest representation of this data is a list of tuples, but you may also use a list of dictionaries, or a list of instances of a custom class.
# from module import CLASS
from datetime import datetime
import requests
import re
import math

def load_rain_data(url):
    data = requests.get(url)
    text = data.text
    rain_data = re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text)
    print(rain_data)


    for i in range(len(rain_data)):
        date = rain_data[i][0]
        daily_total = rain_data[i][1]
        date = datetime.strptime(date, '%d-%b-%Y')

        daily_total = int(daily_total)*0.01 * 2.54

        rain_data[i] = {
            'date': date,
            'daily_total' : daily_total,
        }
    return rain_data

    print(rain_data)

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
    row_highest = rain_data[0]
    for row in rain_data:
        if row['daily_total'] > row_highest['daily_total']:
            row_highest = row
    return row_highest


rain_data = load_rain_data('https://or.water.usgs.gov/non-usgs/bes/yeon.rain')
mean = calc_mean(rain_data)
print(f'\nThe mean of this rain data is {mean}')


variance = calc_var(rain_data, mean)
stan_dev = math.sqrt(variance)
print(f'\n68% of the data falls in a range greater than {mean-stan_dev} and less than {mean+stan_dev}')

row_highest = highest(rain_data)
print(f'\nThe day with the most rain was {row_highest["date"]} with {row_highest["daily_total"]} cm. \n')



# # turn a string into a datetime object
# date = datetime.strptime('25-MAY-2020', '%d-%b-%Y')

# # access the properties of that object
# print(date.year)   # 2016
# print(date.month)  # 3
# print(date.day)    # 25
# print(date)  # 2016-03-25 00:00:00

# # turn the datetime object back into a string
# print(f"Yeon Rain Gage - 3395 NW. Yeon Ave on {date.strftime('%d-%b-%Y')}")  # 25-Mar-2016