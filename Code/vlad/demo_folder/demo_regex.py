# demo_regex #1 April 28 2020:


 
import requests
import re

# get the source code for the google home page
response = requests.get('https://www.google.com')
text = response.text
# print(text)

# get all the hex-encoded colors
pattern = '#[0-9a-fA-F]+'
matches = re.findall(pattern, text)
print(len(matches))
print(matches)