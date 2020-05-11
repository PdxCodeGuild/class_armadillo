# Lab 09 Unit Converter
# Troy Fitzgerald


"""Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters.
Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. 
Below is some sample input/output."""

# imports the module.
import random
import math

# what each distance is by feet.
distance = {'feet': 1, 'meters': 0.3048} 

# len of ft is the distance of 1 ft.
len_of_feet = distance['feet']

# len of m is the distance of 1 m.
len_of_meters = distance['meters']

# has the user ask the distance
user_distance = input('What is the distance in feet?: ')

# the input of the user converting it to a number.
user_distance = int(user_distance)

# the input multiplied by the distance.
total = user_distance * distance['meters']

# the output of the equation.
print(f'The grand total is...{total} meters!')


'''Version 2 - 4'''

# asks the user what distance is.
user_distance = int(input('What is the distance? '))

# asks the user what unit of measurement they would like converted.
user_input = input('What unit would you like to convert? ')

# asks the user what unit of measurement they would like the previous answer converted to .
user_output = input('What unit do you want it converted to? ')

# distance conversions chart.
distance_conversions = {'inches': 0.0254,
                        'feet': 0.3048,
                        'yards': 0.9144,
                        'meters': 1.0,
                        'miles': 1609.34,
                        'kilometers': 1000.0
} 

# formula to convert one unit of measurement to another unit of measurement.
total = user_distance * (distance_conversions[user_input]  /distance_conversions[user_output])

# prints the user output in the new unit of measurement.
print(f'That is equal to...{total}.')