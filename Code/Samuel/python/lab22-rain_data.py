# PDX Code Guild Fullstack Course
# Lab 22 Rain Data
# Samuel Purdy
# 5/1/2020

import requests
import re
import datetime
import math
import matplotlib.pyplot as plt

rain_address = "https://or.water.usgs.gov/non-usgs/bes/glencoe.rain"

# Returns the data from the specified address and cleans up 
# the information while removing parts of it that we don't need.
# address = web address to the site we are using.
def get_data(address):
    format_data = dict()
    data = requests.get(address).text
    
    # locates the line just before the information and cuts out 
    # everything before it including the line..
    data = data[data.find("------------------------------------------------------------------------------------------------------------------")+len("------------------------------------------------------------------------------------------------------------------"):]
    
    # This removes all new lines and spaces as well as grouping 
    # each line of text together into a tuple. The tuple will 
    # contain a date, and a string of numbers and hiphens
    pattern = re.compile(r"([^ \n]+)([^\n]+)")
    listed_data = pattern.findall(data)

    # Loops through the list of tuples and creates a dictionary 
    # with each key being represented by datetime, and each value 
    # being represented by their corresponding list of data.
    for i in range(len(listed_data)):
        date = datetime.datetime.strptime(listed_data[i][0], r"%d-%b-%Y")
        # We don't get rid of the whitespace in the tupled data 
        # only because we can use .split() to make a list of 
        # strings instead and the whitespace is automatically 
        # removed.

        # listed_data is a list of strings that represent the 
        # rain for the whole day at index [0] and each given 
        # hour from index [1]-[24]

        # We use a list of strings purely because some days the 
        # device they use to calculate rain data is sometimes 
        # offline or in need of repair. Each of those hours/days 
        # is represented by a '-' We don't get rid of the days 
        # simply because there are some days where the device in 
        # online for half the day so it would make no sense to do 
        # that.
        format_data.setdefault(date, listed_data[i][1].split())
    return format_data

# Returns the mean of the rain from each day
# rain = dictionary of days and data for each day.
def get_mean(rain):
    total_rain = 0

    # loops through the dictionary and grabs the total rain for 
    # each day and adds it together, while adding the number of
    # days together.
    for day in rain:

        # skips over days with "-" as their data.
        if rain[day][0] != "-":

            # Adds the integer version of the data together.
            total_rain += int(rain[day][0])
    
    # Returns the total rain diveded by the number of days.
    return total_rain / len(rain)

# Returns the standard deviation of the data.
# rain = dictionary of days and data for each day.
def get_standard_deviation(rain):

    # Gets the mean from rain
    mean = get_mean(rain)
    total = 0

    # loops through the dictionary of rainy days, skipping "-" 
    # days, and adds the variance together.
    for day in rain:
        if rain[day][0] != "-":
            total += (float(rain[day][0]) - mean) ** 2

    # Returns the square root of the variance divided by the 
    # number of days to get the standard deviation.
    return math.sqrt(total/len(rain))

# Returns the day with the most rain.
# rain = dictionary of days and data for each day.
def most_rained_day(rain):
    current_day = None

    # Loops through the dictionary of days, if the day is not 
    # None, or the total rain from a given day is greater than 
    # the current day, it will set current_day to the current 
    # looped day.
    for day in rain:
        if rain[day][0] != "-":
            if current_day == None or int(rain[day][0]) > int(rain[current_day][0]):
                current_day = day

    return current_day

# Returns the year with the most rain.
# rain = dictionary of days and data for each day.
def most_rained_year(rain):
    years = dict()

    # Loops through the dictionary, and adds all the total 
    # rain from each day together into the total rain from 
    # each year.
    for day in rain:
        if rain[day][0] != "-":

            # If the year doesnt exist, create a new year 
            # key with the starting value of 0
            years.setdefault(day.year, 0) 
            
            years[day.year] += int(rain[day][0])

    current_year = None

    # Loops through the dictionary of days, if the year is not 
    # None, or the total rain from a given year is greater than 
    # the current year, it will set current_year to the current 
    # looped year.
    for year in years:
        if current_year == None or years[year] > years[current_year]:
            current_year = year

    return current_year

# Uses matplot to make a neat graph to view information.
# rain = dictionary of days and the information from each day.
def make_graph(rain):
    list_of_days = list()
    list_of_rain = list()

    # Loops through the dictionary to generate two lists of 
    # dates and data corresponding to each date.
    for day in rain:
        if rain[day][0] != "-":
            list_of_days.append(day)
            list_of_rain.append(int(rain[day][0]))
    
    # Using those two generated lists, it will create and then 
    # show a graph that has the information from the lists.
    plt.plot(list_of_days, list_of_rain)
    plt.show()

# Tests
if __name__ == "__main__":
    rainy_days = get_data(rain_address)
    mean_of_rainy_days = get_mean(rainy_days)
    rainiest_day = most_rained_day(rainy_days)
    rainiest_year = most_rained_year(rainy_days)
    standard_deviation = get_standard_deviation(rainy_days)

    print(f"The Most Rained Day: {rainiest_day}")
    print(f"The Most Rained Year: {rainiest_year}")
    print(f"The Standard Deviation: {standard_deviation}")
    print(f"Mean of Rainy Days: {mean_of_rainy_days}")

    make_graph(rainy_days)