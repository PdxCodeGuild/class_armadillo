# Take and decipher City of Portland Bureau of Enviromental Services
# rain fall data
from re import findall
import datetime
import statistics
import math
# Open our file and store it as text.
text_path = "C:/Users/talie/class_armadillo/code/talieson/data/rain_data.txt"
with open(text_path, "r") as file:
    text = file.read()


# Use regular expression to identify the date and total amount of rain fall
def find_dates(text):
    data_pattern = (r'(\d+-\w+-\d+)\s+(\d+)')
    # save dates as a list of matcing touples
    dates = findall(data_pattern, text)
    return dates


# Find the mean
def mean(data):
    total = 0
    # loop over the value in the dictionary pair to the total
    for i in list(data.items()):
        total += i[1]
    # divide by the number of items
    mean = total / len(data)
    return mean


def standard_deviation(data, mean_of_data):
    spread = []
    for i in list(data.items()):
        # iterate over our information, subrtact the mean and square it
        (i[1] - mean_of_data) ** 2
        # add the items to spread
        spread.append(i[1])
        # find the sum of the spread
        sum_of_distances = sum(spread)
        # find the variance
        variance = sum_of_distances / len(spread)
        # square root the variance
        standard_deviation = math.sqrt(variance)
    standard_deviation = statistics.pstdev(spread)
    return standard_deviation


def highest_value(data):
    running_highest = 0
    # iterate over values if it's > running highest, it becomes highest
    for i in list(data.items()):
        if i[1] > running_highest:
            running_highest = i[1]
    return running_highest


# call our function
dates = find_dates(text)
# create an empty dictionary to hold our data
data = {}
# iterate over the touples in dates
for date in dates:
    # make the touple a list
    date = list(date)
    # use our strptime to make the date more usable
    date[0] = datetime.datetime.strptime(date[0], '%d-%b-%Y')
    # make our rainfall value into an integer
    date[1] = int(date[1])
    # add to dictionary with date as a key, and the integer as value
    data.update({date[0]: date[1]})

# Call our functions
mean_of_data = mean(data)
standard_deviation_of_data = standard_deviation(data, mean_of_data)
highest_value_in_data = highest_value(data)
