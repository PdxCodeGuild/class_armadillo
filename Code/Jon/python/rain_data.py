import requests
import re
import json
from datetime import datetime

# EXAMPLES
# url = 'https://favqs.com/api/qotd'
# response = requests.get(url)
# # json() Lets you treat it as a dictionary instead of using .text which just makes it a text
# text = response.json()
# print(text['quote']['body'])

# https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain

text = '''            Daily  Hourly data -->
   Date     Total    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
------------------------------------------------------------------------------------------------------------------
04-MAY-2020     0    0   0   0   0   0   0   0   0   0   0
03-MAY-2020    22    0   0   5   3   0   0   0   0   0   0   7   6   0   0   0   0   0   0   1   0   0   0   0   0
02-MAY-2020    30    0   0   0   0   0   1   0   0   6   3   6   4   7   1   0   2   0   0   0   0   0   0   0   0
01-MAY-2020     6    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   4   1   1
30-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
29-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
28-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
27-APR-2020     3    0   2   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
26-APR-2020     5    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   2   3   0
25-APR-2020    16    0   0   0   0   0   0   5   8   2   0   0   0   0   0   0   1   0   0   0   0   0   0   0   0
24-APR-2020     2    0   0   0   0   0   0   0   0   1   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0
23-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
22-APR-2020    23    0   0   0   0   2   4   0   3   6   3   0   4   0   0   1   0 '''

# use string operations to parse the rain file

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/skyline_school.rain')
# print(response.text)
lines = response.text.split('\n')
lines = lines[11:] # chop off the junk at the start
for line in lines:
    print(line.split())


# or use regular expressions
# https://regex101.com/r/QwMfRM/1



# get all the rain data on the site
def get_rain_file_urls():
    response = requests.get('https://or.water.usgs.gov/non-usgs/bes/')
    text = response.text
    rain_files = re.findall(r'\w+\.rain', text)
    rain_files = ['https://or.water.usgs.gov/non-usgs/bes/' + rain_file for rain_file in rain_files]
    return rain_files

def get_rain_data(url):
    # your code here
    print(url)
    pass

rain_file_urls = get_rain_file_urls()
for rain_file_url in rain_file_urls:
    data = get_rain_data(rain_file_url)
    print(data)

exit()

