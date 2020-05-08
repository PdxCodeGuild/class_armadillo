import requests
import re
from math import sqrt
import matplotlib.pyplot as plt
from datetime import datetime


data = requests.get("https://or.water.usgs.gov/non-usgs/bes/gresham.rain").text

# split data by line and remove the chunk 'o' junk
# at the beginning that isn't rain data
data = data.split('\n')[11:]

cleaned_data = {}
for i in range(len(data) - 1):
    # replace two or more spaces with a single space and
    cleaned_row = re.split(r'\s{2,}', data[i])

    # cleaned_row = [date, daily rainfall]
    # if no total was present for that day, the total is represented by
    # a hyphen, we'll skip those entries
    # if a total is present, create a dictionary entry for it
    if cleaned_row[1] == '-':
        continue
    else:
        cleaned_data.setdefault(cleaned_row[0], int(cleaned_row[1]))

rain_data = {}

for date, value in cleaned_data.items():
    date = datetime.strptime(date, '%d-%b-%Y')
    
    year = date.year
    month = date.month
    day = date.day

    rain_data.setdefault(year, {})
    rain_data[year].setdefault(month, {})
    rain_data[year][month].setdefault(day, value)
    
    # rain_data.setdefault(date.year, {})


# sum of all totals divided by total number of entries
mean = sum(cleaned_data.values()) / len(cleaned_data)
print(f"Average rainfall: {round(mean, 2)}")

# difference of each item and the mean squared divided by total number of entries
variance = sum([(i - mean) ** 2 for i in cleaned_data.values()]) / len(cleaned_data)
print(f"Variance: {variance}")

# square root of the variance
standard_deviation = sqrt(variance)
print(f"Standard deviation: {standard_deviation}")



options = {
    '1': 'All dates and rainfall totals',
    '2': 'Average monthly total across all years',
    '3': 'Total yearly rainfall, year by year'
}

while True:
    print()
    for option in options:
        print(f'{option}: {options[option]}')

    choice = input("\nWhich graph would you like to view?")
    while choice not in options:
        print("Please select the number of the option you'd like.")
        choice = input("Which graph would you like to view?")

    if choice == '1':
        plt.ylabel('Total rainfall')
        plt.xlabel('Date')

        plt.plot(list(cleaned_data.keys()), list(cleaned_data.values()))
        plt.show()

    elif choice == '2':
        plt.ylabel('Average Rainfall')
        plt.xlabel('Month/Year')
        averages = {}
        for year in rain_data:
            for month in rain_data[year]:
                all_days = list(rain_data[year][month].values())
                total_rain = sum(all_days)
                averages.setdefault(f'{year}/{month}', total_rain / len(all_days))
        plt.plot(list(averages.keys()), list(averages.values()))
        plt.show()

    elif choice == '3':
        plt.ylabel('Average Yearly Rainfall')
        plt.xlabel('Year')

        yearly_avgs = {}
        for year in rain_data:
            yearly_avg = 0
            for month in rain_data[year]:
                for day in rain_data[year][month]:
                    yearly_avg += rain_data[year][month][day]
            yearly_avgs.setdefault(year, yearly_avg)

        plt.plot(list(yearly_avgs.keys()), list(yearly_avgs.values()))
        plt.show()


    again = input('Would you like to view another graph? y/n: ')
    while again not in ['y', 'n']:
        print('Invalid entry')
        again = input('Would you like to view another graph? y/n: ')

    if again == 'y':
        continue
    else:
        print('K. Bye!')
        break