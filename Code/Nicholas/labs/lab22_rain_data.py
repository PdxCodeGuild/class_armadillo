# Eco Roof Rain Gage - SW 12th and Clay

# PROVISIONAL, UNCORRECTED RAW DATA FROM THE CITY OF PORTLAND HYDRA NETWORK.
# Data are the number of tips of the rain gage bucket.
# Each tip is 0.01 inches of rainfall.
#  [-, missing data]
# Dates and times are PACIFIC STANDARD TIME.
from datetime import datetime 
import re
import requests

response = requests.get('https://or.water.usgs.gov/non-usgs/bes/twelfth_and_clay.rain')
text = response.text


x = re.findall(r"(\d+\D\w+\D\d+)\s+(\d+)", text)
rain_data = []
for dates in x:
    dates = datetime.strptime(dates[0], '%d-%b-%Y')
    rain_data.append(dates)


print(rain_data)








