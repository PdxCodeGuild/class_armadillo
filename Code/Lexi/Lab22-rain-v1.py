# from module import CLASS
from datetime import datetime
import requests
import re

#https://www.w3schools.com/python/ref_requests_response.asp
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')
text = response.text

def get_rain(text): # create function
    #https://www.w3schools.com/python/python_regex.asp
    #https://docs.python.org/3/library/re.html
    # parantheses are diff capture groups
    return re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text)
    # had an 'unbalanced parenthesis error on line 938
date = get_rain(text) # calls function
#print(date) # checking if re.findall worked

rain_data = []
for day in date: 
    #https://www.journaldev.com/23365/python-string-to-datetime-strptime
    # making an object
    # %Y	Year with century as a decimal number.
    rain = datetime.strptime(day[0], '%d-%b-%Y'), int(day[1])
    # %b	Month as locale’s abbreviated name.
    rain_data.append(rain) # adds date to empty list we created

print(rain_data)

# create empty list
# go through all days
# for day in date:
#     date.
