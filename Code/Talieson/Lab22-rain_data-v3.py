# Take and decipher City of Portland Bureau of Enviromental Services
# rain fall data
from re import findall
import matplotlib.pyplot as plt
from collections import OrderedDict

# Open our file and store it as text.
text_path = "C:/Users/talie/class_armadillo/code/talieson/data/rain_data.txt"
with open(text_path, "r") as file:
    text = file.read()
location_pattern = (r'\A.*')
location = findall(location_pattern, text)


# Use regular expression to identify the date and total amount of rain fall
def find_dates(text):
    data_pattern = (r'(\d+-\w+-\d+)\s+(\d+)')
    # save dates as a list of matcing touples
    dates = findall(data_pattern, text)
    return dates


def rain_by_data(data):
    # make our data into a list for the pyplot function
    x = list(data.keys())
    y = list(data.values())
    # label our graph and axis
    plt.xlabel("Date")
    plt.ylabel("Rainfall (in 100ths of an inch)")
    plt.title(f"Rain fall per day at {location}")
    plt.plot(x, y)
    plt.show()


def rain_by_year(data, year):
    year_dict = OrderedDict()
    for key, value in data:
        if year in key:
            year_dict.update(key, value)
    x = list(year_dict.keys())
    y = list(year_dict.values())
    # label our graph and axis
    plt.xlabel(f"Date in {year}")
    plt.ylabel("Rainfall (in 100ths of an inch)")
    plt.title(f"Rain fall per day at {location}")
    plt.plot(x, y)
    plt.show()


dates = find_dates(text)

# create an empty dictionary to hold our data
data = OrderedDict()
# iterate over the touples in dates
for date in dates:
    # make the touple a list
    date = list(date)
    # make our rainfall value into an integer
    date[1] = int(date[1])
    # add to dictionary with date as a key, and the integer as value
    data.update({date[0]: date[1]})
    data.move_to_end(date[0], last=False)

while True:
    year = input("Which year do you want rain data from? ")
    if year.isdigit():
        year = int(year)
    else:
        print("please enter a valid year in digits. ex: <XXXX>")

    # Call our function
    rain_by_year(data, year)
