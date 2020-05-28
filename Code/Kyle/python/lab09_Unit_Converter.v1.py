# Version 1
# Ask the user for the number of feet, and print out the equivalent distance in meters. 
# Hint: 1 ft is 0.3048 m.
#converted_to_meters = ""

def unit_converter(int1):
    converted_to_meters = float(how_many_feet) * 0.3048 #multiply feet by conversion factor and change to float
    converted_to_meters_rounded = round(converted_to_meters, 2) #round the decimal to 3 places
    print(f'{how_many_feet} is {converted_to_meters} meters')


print("Let's convert imperial to metric.")
how_many_feet = input("What is the measurement distance in feet? ")

unit_converter(how_many_feet)