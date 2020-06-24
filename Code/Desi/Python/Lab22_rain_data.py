from datetime import datetime
import re
import requests
import math

# turn a string into a datetime object
date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')

# access the properties of that object
print(date.year)   # 2016
print(date.month)  # 3
print(date.day)    # 25
print(date)  # 2016-03-25 00:00:00

# turn the datetime object back into a string
print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016






# define the path and open text file

# gets data from website
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/metro_center.rain') # gets data from website
text = response.text #turns into text format