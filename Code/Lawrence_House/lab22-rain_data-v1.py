import datetime
import requests
import re

# Url method of grabbing data

# url = ('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')

# request_data = requests.get(url)
# text = request_data.text

# Text file method of grabbing data

filename = 'Code\Lawrence_House\hayden_island.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

# Regular expression for finding date and total rainfall

regex = r"(\d+-\w+-\d+)\s+(\d+)"
match = re.findall(regex, text)
print(match)