



import requests
from datetime import datetime
import re
import math


# date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')

url = requests.get('https://or.water.usgs.gov/non-usgs/bes/multnomah.rain')

multnomah_rain = url.text
# get the rain-fall



# Use regular expression to identify the date and total amount of rain fall

def day_in_month(multnomah_rain):

    # get the date
    # listy = []
    # get just the total rainfalls
    monthly_rain = re.findall(r'\d+-\w+-\d+\s+(\d+)', multnomah_rain)
    # get just the dates
    monthly_date = re.findall(r'\d+-\w+-\d+', multnomah_rain)
    # iterated over the rainfalls and joined them into a list of tuples.
    for i in range(len(monthly_rain)):
        # date = datetime.strptime(monthly_date[i], '%d-%b-%Y')
        rain_fall_amount = int(monthly_rain[i])
        # print(date)
        tuples = (monthly_date[i],rain_fall_amount)
        # tuples = listy.append(tuples)
        total_rain_fall = 0
        for i in rain_fall_amount:
            total_rain_fall += rain_fall_amount[i]
            total_rain_fall/rain_fall_amount = wow
            print(wow)

        print(tuples)
        # print(listy)
    
    # call our function
day_in_month(multnomah_rain)



