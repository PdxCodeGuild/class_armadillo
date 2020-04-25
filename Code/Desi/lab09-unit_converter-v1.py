import math
import time

#variable setting


conversions = {
    "ft": .3048,
    "m": 1,
    "mi": 1609.34,
    "km": 1000,
    "yd": 0.9144,
    "in": .0254,

}


unit1 = input("Which unit would you like to convert from: ")
unit2 = input("Which unit would you like to convert to: ")
num = float(input("Enter your value: " ))

calculations = num * conversions[unit1]
calculation2 = calculations/conversions[unit2]
result = f'{num} {unit1} is equal to {calculations}{unit2}'
print("\n")
print(result)





# Lab 9: Unit Converter

# This lab will involve writing a program that allows the user to convert a number between units.

# ## Version 1

# Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by **multiplying the input distance by 0.3048**. Below is some sample input/output.

# ```
# > what is the distance in feet? 12
# > 12 ft is 3.6576 m
# ```