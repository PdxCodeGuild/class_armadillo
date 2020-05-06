# Lab 09 a simple Unit coversion

# Import time is being used to allow the user to read the welcome message,
# the order of entery for the converter, and the units of messure
import time

# I am using a dictionary to pull the inofrmation for the unit converter.
# all enties are converted to meters.
units = {
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.34,
    "m": 1,
    "km": 1000}

# Welcome message that is printed at the start of the program 
print("Welcome to the Unit Conveter \n")
time.sleep(1)

# Order of information entry
print("Please enter the distance, \n", 
"Then Unit of Disatance, \n", 
"Then Press Enter \ Return\n")
time.sleep(2)

# Units of messure
print(
"in, \n"
"ft,\n"
"yd, \n"
"mi,\n"
"m,\n"
"km\n")

# This is the functional part of the program, mainly driven off of user input and then printing the results 
distance = int(input("Enter your distance/length: "))
unit = input("Enter the unit to convert from: in, ft, yd, mi, m, km: ")
result = distance * units[unit]
print(f"There is {result} meter(s) in {distance} {unit}(s)")