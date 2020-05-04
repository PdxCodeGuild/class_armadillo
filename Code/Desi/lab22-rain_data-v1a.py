from datetime import datetime
import re 
import requests

# define the path and open text file

# gets data from website
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/metro_center.rain') # gets data from website
text = response.text #turns into text format

def rain_data(text): # function 
    return re.findall(r'(\d+-\w+-\d+)\s+(\d+)', text) # regular expression we want to find EVERYTHING that fits this criteria
        # \d means digits
        # \w means words
        # \s means space
        # () means capture groups - we are splitting it into these groups

dates = rain_data(text) # calls above function
rain_list = [] # empty list for collecting formatted date tuples from below loop
for date in dates: # iterates through each tuplet(date)of the 'dates' list
    rain = (datetime.strptime(date[0], '%d-%b-%Y')), int(date[1]) # transforms date in each tuple to date objects
    rain_list.append(rain) # adds date formatted tuples to list

print(rain_list)


#             Daily  Hourly data -->
#    Date     Total    0   1   2   3   4   5   6   7   8   9  10  11  12  13  14  15  16  17  18  19  20  21  22  23
# ------------------------------------------------------------------------------------------------------------------
# 01-MAY-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 30-APR-2020     6    0   0   0   0   0   0   0   0   1   0   0   2   2   1   0   0   0   0   0   0   0   0   0   0
# 29-APR-2020     3    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1   1   0   1   0   0   0   0   0
# 28-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 27-APR-2020     2    1   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 26-APR-2020     6    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   1   4   1
# 25-APR-2020    33    0   0   0   0   0   0   5  15   2   1   0   0  10   0   0   0   0   0   0   0   0   0   0   0
# 24-APR-2020     4    0   0   0   0   0   0   0   0   3   1   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 23-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 22-APR-2020    32    0   0   0   0   2   3   0   2   9   3   0   5   0   1   6   0   0   0   0   0   0   1   0   0
# 21-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 20-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 19-APR-2020     1    0   0   0   0   0   0   0   0   0   0   1   0   0   0   0   0   0   0   0   0   0   0   0   0
# 18-APR-2020     7    0   0   0   0   0   0   0   1   0   1   2   2   0   0   0   1   0   0   0   0   0   0   0   0
# 17-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# 16-APR-2020     0    0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0   0
# '''



data = [{ 
          "date": (2020, 5, 1),
          "time": 0
},{
          "date": (2020, 4, 30),
          "time": 0
},{          
          "date": (2020, 4,25),
          "time": 16
}]