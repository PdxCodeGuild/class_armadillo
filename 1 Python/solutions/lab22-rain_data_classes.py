

import requests
import re
import datetime

class RainDataRow:
    def __init__(self, date, daily_total, hourly):
        self.date = date
        self.daily_total = daily_total
        self.hourly = hourly


class RainData:
    def __init__(self, text):

        self.data = []
        self.units = 'tips'

        lines = text.split('\n')
        lines = lines[11:]
        for line in lines:
            values = line.split()
            if len(values) == 0:
                continue

            date = RainData.parse_date(values[0])
            daily_total = RainData.parse_tips(values[1])
            hourly = values[2:]
            hourly = [RainData.parse_tips(hour_value) for hour_value in hourly]
            if len(hourly) < 24:
                hourly += [0] * (24 - len(hourly))

            rain_data_row = RainDataRow(date, daily_total, hourly)
            self.data.append(rain_data_row)

        total = 0
        count = 0
        for data_row in self.data:
            if data_row.daily_total != None:
                total += data_row.daily_total
                count += 1

    @staticmethod
    def parse_date(date_str):
        return datetime.datetime.strptime(date_str, '%d-%b-%Y')

    @staticmethod
    def parse_tips(int_str):
        return float(int_str) if int_str != '-' else None

    def convert_tips_to_cm(self):
        if self.units != 'tips':
            return
        for data_row in self.data:
            if data_row.daily_total is not None:
                data_row.daily_total *= 0.01*2.54
            data_row.hourly = [hourly_value*0.01*2.54 if hourly_value is not None else None for hourly_value in data_row.hourly]
        self.units = 'cm'


    def get_years(self):
        years = set()
        for data_row in self.data:
            years.add(data_row.date.year)
        years = list(years)
        years.sort()
        return years


url = 'https://or.water.usgs.gov/non-usgs/bes/'
def get_locations():
    r = requests.get(url)
    locations = re.findall(r'(\w+)\.rain', r.text)
    locations.sort()
    return locations

def get_file(location):
    r = requests.get(url + location + '.rain')
    return r.text




print('getting locations...')
locations = get_locations()
print('downloading file...')
text = get_file(locations[1])

rain_data = RainData(text)
print(rain_data.units)
rain_data.convert_tips_to_cm()
print(rain_data.units)






