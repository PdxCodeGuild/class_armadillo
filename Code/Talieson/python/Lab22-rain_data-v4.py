# Take and decipher City of Portland Bureau of Enviromental Services
# rain fall data
import requests
from re import findall
import matplotlib.pyplot as plt
from collections import OrderedDict


# get all the rain data on the site
def get_rain_file_urls():
    response = requests.get('https://or.water.usgs.gov/non-usgs/bes/')
    text = response.text
    rain_files = findall(r'\w+\.rain', text)
    rain_files = ['https://or.water.usgs.gov/non-usgs/bes/' + rain_file for rain_file in rain_files]
    return rain_files


def get_rain_location(url):
    data_response = requests.get(url)
    text_response = data_response.text
    location_pattern = (r'\A.*')
    location = findall(location_pattern, text_response)
    location = str(location)
    return location


# Use regular expression to identify the date and total amount of rain fall
def find_dates(rain_data_dictionary, user_loc):
    response = requests.get(rain_data_dictionary[user_loc][1])
    text = response.text
    data_pattern = (r'(\d+-\w+-\d+)\s+(\d+)')
    # save dates as a list of matcing touples
    dates = findall(data_pattern, text)
    return dates


def rain_by_data(data, title):
    # make our data into a list for the pyplot function
    x = list(data.keys())
    y = list(data.values())
    # call our function to creat the graph
    gen_graph(x, y, title)


def rain_by_date(data, date, title):
    # dictionary with just the values we want
    date_dict = {}
    for key, value in data.items():
        if date in key:
            date_dict.update({key: value})
    x = list(date_dict.keys())
    y = list(date_dict.values())
    # call our function to creat the graph
    gen_graph(x, y, title, date)


# takes x, y from other functions, styles graph
def gen_graph(x, y, title, date="Recorded History"):
    plt.xlabel(f"Date in {date}")
    plt.ylabel("Rainfall (in 100ths of an inch)")
    plt.title(f"Rain fall per day at {title}")
    plt.plot(x, y, "-bo", markevery=None)
    plt.show()


print('''
            ***************************************
            Please wait while data is loaded...
            ***************************************
''')

rain_data_dictionary = {}
data_dictionary_count = 0
rain_file_urls = get_rain_file_urls()
for rain_file_url in rain_file_urls:
    data_dictionary_count += 1
    location = get_rain_location(rain_file_url)
    rain_data_dictionary.update({data_dictionary_count: (location, rain_file_url)})

for key, value in rain_data_dictionary.items():
    print(f"{key} {value[0]}")
user_loc = input('''
Enter the number of the location you'd like to view data for.
    > ''')
if user_loc.isdigit():
    user_loc = int(user_loc)
    graph_title = rain_data_dictionary[user_loc][0]
    print(graph_title)

dates = find_dates(rain_data_dictionary, user_loc)

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
        rain_by_data(data, graph_title)
    elif operation == '2':
        year = input('''3
Enter 4 digit year or uppercase 3 letter month appreviation:
    > ''')
        rain_by_date(data, year, graph_title)
    elif operation == '3':
        year_month = input('''
enter in uppercase 3 letter appreviation - year. ex: <MAY-2020>
    > ''')
        rain_by_date(data, year_month, graph_title)
    elif operation == 'E':
        exit()
    else:
        print('''
        ERROR: Not a valid input!
        ''')
