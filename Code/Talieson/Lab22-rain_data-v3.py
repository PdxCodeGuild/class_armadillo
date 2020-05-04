# Take and decipher City of Portland Bureau of Enviromental Services
# rain fall data
from re import findall
import matplotlib.pyplot as plt
from collections import OrderedDict

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


def rain_by_data(data):
    # make our data into a list for the pyplot function
    x = list(data.keys())
    y = list(data.values())
    # call our function to creat the graph
    gen_graph(x, y)


def rain_by_date(data, date):
    # dictionary with just the values we want
    date_dict = {}
    for key, value in data.items():
        if date in key:
            date_dict.update({key: value})
    x = list(date_dict.keys())
    y = list(date_dict.values())
    # call our function to creat the graph
    gen_graph(x, y, date)


# takes x, y from other functions, styles graph
def gen_graph(x, y, date="Recorded History"):
    plt.xlabel(f"Date in {date}")
    plt.ylabel("Rainfall (in 100ths of an inch)")
    plt.title(f"Rain fall per day at {location}")
    plt.plot(x, y, "-bo", markevery=None)
    plt.show()


dates = find_dates(text)
location_pattern = (r'\A.*')
location = findall(location_pattern, text)

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
    operation = input('''Enter the number for the operation you would you like to peform:
        1: rainfall by date for all recorded history.
        2: rainfall by month or year.
        3: rainfall by month of a specific year.
        E: Exit.
            > ''')
    if operation == '1':
        rain_by_data(data)
    elif operation == '2':
        year = input('''
Enter 4 digit year or uppercase 3 letter appreviation:
    > ''')
        rain_by_date(data, year)
    elif operation == '3':
        year_month = input('''
enter in uppercase 3 letter appreviation - year. ex: <MAY-2020>
    > ''')
        rain_by_date(data, year_month)
    elif operation == 'E':
        exit()
    else:
        print('''
        ERROR: Not a valid input!
        ''')
