

import requests
import re


response = requests.get('https://or.water.usgs.gov/non-usgs/bes/skyline_school.rain')
# print
lines = response.text.split('\n')

for line in lines:
    print(line.split())



