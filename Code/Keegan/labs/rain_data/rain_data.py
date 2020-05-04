import requests
import re
from math import sqrt


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

# sum of all totals divided by total number of entries
mean = sum(cleaned_data.values()) / len(cleaned_data)
print(f"Average rainfall: {round(mean, 2)}")

# difference of each item and the mean squared divided by total number of entries
variance = sum([(i - mean) ** 2 for i in cleaned_data.values()]) / len(cleaned_data)
print(f"Variance: {variance}")

# square root of the variance
standard_deviation = sqrt(variance)
print(f"Standard deviation: {standard_deviation}")