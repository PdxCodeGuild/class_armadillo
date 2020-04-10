#Lab 9: Unit Converter
""" This lab will involve writing a program that allows the user to convert a number between units.

Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m
Version 2
Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m 
"""

units = {
    'ft': .3048,
    'm': 1,
    'mi': 1609.34,
    'km': 1000,
}


num = int(input("Please enter a number to convert into meters: "))
c_unit = input("Would you please enter the unit to convert from: ")


product = num * units[c_unit]
result = f'{num} {c_unit} is equal to {product} meters '
print(result)