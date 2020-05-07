​

​

import requests

import re

​

# use string operations to parse the rain file

​

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/skyline_school.rain')

# print(response.text)

lines = response.text.split('\n')

lines = lines[11:] # chop off the junk at the start

for line in lines:

    print(line.split())

​

​

# or use regular expressions

# https://regex101.com/r/QwMfRM/1

​

​

​

# get all the rain data on the site

def get_rain_file_urls():

    response = requests.get('https://or.water.usgs.gov/non-usgs/bes/')

    text = response.text

    rain_files = re.findall(r'\w+\.rain', text)

    rain_files = ['https://or.water.usgs.gov/non-usgs/bes/' + rain_file for rain_file in rain_files]

    return rain_files

​

def get_rain_data(url):

    # your code here

    print(url)

    pass

​

rain_file_urls = get_rain_file_urls()

for rain_file_url in rain_file_urls:

    data = get_rain_data(rain_file_url)

    print(data)

​

exit()

​