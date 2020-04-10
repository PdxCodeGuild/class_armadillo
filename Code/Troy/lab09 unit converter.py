"""Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters.
Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. 
Below is some sample input/output."""

import random
import math
import time


# what each distance is by feet
distance = {'feet': 1, 'meters': 0.3048} 

# len of ft is the distance of 1 ft
len_of_feet = distance['feet']

# len of m is the distance of 1 m
len_of_meters = distance['meters']

# has the user ask the distance
user_distance = input('What is the distance in feet?: ')

# the input of the user converting it to a number
user_distance = int(user_distance)

# the input multiplied by the distance
total = user_distance * distance['meters']

# the output of the equation
print(f'The grand total is...{total}')


'''Version 2 - 4'''

user_distance= int(input('What is the distance? '))
user_input = input('What unit would you like to convert? ')
user_output = input('What unit do you want it converted to? ')
# print('That converts to...')

distance_conversions = {'inches': 0.0254,
                        'feet': 0.3048,
                        'yards': 0.9144,
                        'meters': 1,
                        'miles': 1609.34,
                        'kilometers': 1000
} 


total = user_distance * (distance_conversions[user_input]  /distance_conversions[user_output])

print(f"The grand total is...{total}")