"""

Lab 9: Unit Converter

This lab will involve writing a program that allows the user to convert a number between units.

Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m

"""

import time

print("Let's talk about converting a number between units... ")

time.sleep(1)

print("Let's begin by converting feet to meters... ")

time.sleep(1)

feet = float(input("Please enter a length in feet: ex. 5 "))

meters = feet*0.3048

time.sleep(1)

print(f"{feet} feet is equivalent to {meters} meters")