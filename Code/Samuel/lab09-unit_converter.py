# PDX Code Guild Fullstack Course
# Lab 09 Unit Converter
# Samuel Purdy
# 4/9/2020

# Dictionary of unit types, their conversion to meters, and converting a meter into that unit.
unit_conversions = {
    "Feet": [0.3048, 3.2808],
    "Miles": [1609.34, 0.0006],
    "Meters": [1,1],
    "Kilometers": [1000, 0.001],
    "Yards": [0.9144, 1.0936],
    "Inches": [0.0254, 39.3701]
}

# Initilizing variables
valid_input = False
user_input = "u"
input_units = "u"
output_units = "u"

# Prints the list of unit types.
print("These are the types of units you can select from")
for units in unit_conversions:
    print(units)

# Asks the user for the input, while checking to see if the user input is a proper input.
while user_input.isnumeric() != True or int(user_input) < 1:
    user_input = input("What is the distance? ")

# Checks to see if the user had input the correct type of units.
while valid_input != True:
     input_units = input("What are the input units? ")
     for units in unit_conversions:
         if units == input_units:
            valid_input = True
            break

# Resets to help verify the output units.
valid_input = False

# Checks to see if the user had input the correct type of units.
while valid_input != True:
     output_units = input("What are the Output units? ")
     for units in unit_conversions:
         if units == output_units:
            valid_input = True
            break

# Checks to see if the user had input the same type of units, to avoid decimals if the unit types are the same.
if input_units == output_units:
    print(f"{user_input} {input_units} is {user_input} {output_units}")
else:
    # Does math based on turning the users input into meters, then back into the desired output unit.
    print(f"{user_input} {input_units} is {round((float((unit_conversions[input_units][0] * int(user_input)) * unit_conversions[output_units][1])), 2)} {output_units}")