import requests
import re
from datetime import datetime

# Pulling the data fromt the website.
response = requests.get('https://or.water.usgs.gov/non-usgs/bes/walmart_ecoroof.rain') # gets data from website
# turns into text format
text = response.text

# Getting the data for each date and the daily total
pir_rain_gauge = re.findall(r"(\d+-\w+-\d+) \s+ (\d+)", text)
# print(pir_rain_gauge)

date = datetime.strptime("07-APR-2019", "%d-%b-%Y")

print(date.year)
print(date.month)
print(date.day)
print(date)
 