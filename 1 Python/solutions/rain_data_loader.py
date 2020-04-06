
import re
import requests

url = 'https://or.water.usgs.gov/non-usgs/bes/'


def get_locations():
    r = requests.get(url)
    locations = re.findall(r'\w+\.rain', r.text)
    locations.sort()
    return locations


def get_file(location):
    r = requests.get(url + location)
    return r.text


locations = get_locations()

print('which location would you like to see?')
for i in range(len(locations)):
    print(f'\t{i} {locations[i]}')

location_index = int(input('> '))

print(get_file(locations[location_index]))