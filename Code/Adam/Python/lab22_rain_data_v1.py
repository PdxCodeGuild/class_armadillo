"""
Lab 21: Rain Data

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

Download one of these files and write a function to load the file. The two 
columns that are most important are the date and the daily total. The simplest 
representation of this data is a list of tuples, but you may also use a list of 
dictionaries, or a list of instances of a custom class.

To parse the dates, use datetime.strptime. This allows for easy access to the 
year, month, and day as ints. Below I've shown how to parse an example string, 
resulting in a datetime object. We can then access the year, month, and day on 
that datetime as ints. Later, if you want to print the datetime in a more 
human-readable format, you can use datetime.strftime.

import datetime
date = datetime.datetime.strptime('25-MAR-2016', '%d-%b-%Y')
print(date.year)   # 2016
print(date.month)  # 3
print(date.day)    # 25
print(date)  # 2016-03-25 00:00:00
print(date.strftime('%d-%b-%Y'))  # 25-Mar-2016

"""


​
text = '''
Hayden Island Rain Gage - 1740 N. Jantzen Beach Ctr.
​
PROVISIONAL, UNCORRECTED RAW DATA FROM THE CITY OF PORTLAND HYDRA NETWORK.
Data are the number of tips of the rain gage bucket.
Each tip is 0.01 inches of rainfall.
 [-, missing data]
Dates and times are PACIFIC STANDARD TIME.
​
            Daily  Hourly data -->
   Date     Total    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
------------------------------------------------------------------------------------------------------------------
01-MAY-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0
30-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
29-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
28-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
27-APR-2020     3    0   2   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
26-APR-2020     5    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   2   3   0
25-APR-2020    16    0   0   0   0   0   0   5   8   2   0   0   0   0   0   0   1   0   0   0   0   0   0   0   0
24-APR-2020     2    0   0   0   0   0   0   0   0   1   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0
23-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
22-APR-2020    23    0   0   0   0   2   4   0   3   6   3   0   4   0   0   1   0   0   0   0   0   0   0   0   0
21-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
20-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
19-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
18-APR-2020    18    0   0   0   0   0   0   0   0   1   1   1   2   0   0   1   1   0   4   6   0   0   0   0   1
17-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
16-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
15-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
'''


​import requests


from datetime import datetime
​
# use string operations to parse the rain file

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/skyline_school.rain')
# print(response.text)
lines = response.text.split('\n')
lines = lines[11:] # chop off the junk at the start
for line in lines:
    print(line.split())
​
​
# represent data as a list of dictionaries, with a tuple for the date
data = [{
    'date': (2020, 5, 1),
    'total': 0
},{
    'date': (2020, 4, 30),
    'total': 0
},
...
{
    'date': (2020, 4, 25),
    'total': 16
}]
​
# represent data as a list of tuples with datetime objects
data = [
    (datetime(2020, 5, 1), 0),
    (datetime(2020, 4, 30), 0)
]
​
# represent the data as a list of instances of DailyRain
class DailyRain:
    def __init__(self, date, total):
        self.date = date
        self.total = total
​
Collapse





