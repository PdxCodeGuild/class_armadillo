

import requests
import re
import datetime


url = 'https://or.water.usgs.gov/non-usgs/bes/'
def get_locations():
    r = requests.get(url)
    locations = re.findall(r'(\w+)\.rain', r.text)
    locations.sort()
    return locations

def get_file(location):
    r = requests.get(url + location + '.rain')
    return r.text

def parse_date(date_str):
    return datetime.datetime.strptime(date_str, '%d-%b-%Y')


print('getting locations...')
locations = get_locations()
print('downloading file...')
text = get_file(locations[1])

print('parsing text...')
data = re.findall('(\d{2}-\w{3}-\d{4}) +(\d+)', text)

data = [(parse_date(data[i][0]), int(data[i][1]) * 0.01 * 2.54) for i in range(len(data))]



total = sum([row[1] for row in data])
print(total / len(data))



max_value = -1
for row in data:
    if row[1] > max_value:
        max_value = row[1]
print(max_value)

max_value = max([row[1] for row in data])


years = [2018, 2017, 2016]
totals = [450, 432, 242]
counts = [365, 365, 330]

print(f'for {years[2]} the average was {totals[2]/counts[2]}')


yearly_data = {
    2018: {'total': 450, 'count': 365},
    2017: {'total': 450, 'count': 365},
    2016: {'total': 450, 'count': 365}
}

yearly_data = [{'year':2018, 'total':450, 'count':365}]


years = {row[0].year for row in data}
print(years)

years = []
for row in data:
    if row[0].year not in years:
        years.append(row[0].year)
years.sort()









