import requests 
import re

# v1
# 1) load the data from the rain data website, either using requests or with open...
# 2) transform the data into a list of tuples or a list of dictionaries
#    turn the daily total into an integer and the date into a datetime object (strptime)
# 3) do some calculations on the data (v2)
# 4) make some fancy charts (v3)


response = requests.get('http://or.water.usgs.gov/non-usgs/bes/')



lines = response.text.split('\n')

lines = lines[11:]
data = []
for line in lines:
    if lines == '':
        continue
    #print(line)
    row = line.split()
    print(row)
    break
date = row[0]
total = row[1]


