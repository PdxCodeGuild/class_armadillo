"""
Lab 22: Rain Data

The 'City of Portland Bureau of Environmental Services' operates and maintains 
a network of rain gauges around Portland, and publishes their data publicly: 
http://or.water.usgs.gov/non-usgs/bes/

The data tables available on the site look something like...

Daily  Hourly data -->

   Date     Total    0   1
--------------------------
25-MAR-2016     0    0   0
24-MAR-2016     6    0   1
23-MAR-2016     -    -   -
MORE...

Version 1
Download or use requests to get these files. The two columns that are most 
important are the date and the daily total. The simplest representation of this
data is a list of tuples, but you may also use a list of dictionaries, or a 
list of instances of a custom class.

To parse the dates, use datetime.strptime. This allows for easy access to the 
year, month, and day as ints. Below I've shown how to parse an example string, 
resulting in a datetime object. We can then access the year, month, and day on 
that datetime as ints. Later, if you want to print the datetime in a more 
human-readable format, you can use datetime.strftime.

"""
from datetime import datetime
import requests
import re


print('Sylvania PCC Rain Gage') 

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/pcc_sylvania.rain')
data = response.text
# print(data)

# using regex to isolate the date pattern and first column of daily totals
date_n_dtotal = re.findall('(\d+-\w+-\d+)\s+(\d+)', data)
print(date_n_dtotal)


# # turn a string into a datetime object
# date = datetime.strptime('25-MAR-2016', '%d-%b-%Y')


# # access the properties of that object
# print(f'date.year: {date.year}')   # 2016
# print(f'date.month: {date.month}')  # 3
# print(f'date.day: {date.day}')    # 25
# print(f'date:{date}')  # 2016-03-25 00:00:00

# # turn the datetime object back into a string
# print(f"date.str('%d-%b-%Y'): {date.strftime('%d-%b-%Y')}")  # 25-Mar-2016