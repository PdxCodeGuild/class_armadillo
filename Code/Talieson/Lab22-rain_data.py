# Take and decipher City of Portland Bureau of Enviromental Services
# rain fall data
from re import findall
import datetime

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

# datetime.strftime prints the date in a more user friendly manner
# print(list(data)[0])
# list(d.values())
# print(data)
