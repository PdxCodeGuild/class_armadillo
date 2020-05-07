import datetime
import requests
import re

# url = ('https://or.water.usgs.gov/non-usgs/bes/hayden_island.rain')

# request_data = requests.get(url)
# hayden_island = request_data.text
# print(hayden_island)

filename = 'Code\Lawrence_House\hayden_island.txt'
file = open(filename, 'rt')
text = file.read()
file.close()

regex = r"(\d+-\w+-\d+)\s+(\d+)"
match = re.findall(regex, text)
print(match)

regex = r"\b((?!=|\.).)+(.)\b"

sentences = re.findall(regex, text)

print(sentences)