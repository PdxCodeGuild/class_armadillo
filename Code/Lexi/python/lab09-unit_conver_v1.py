# Lab 09 v2

# Ask the user for the number of feet, and
#  print out the equivalent distance in meters. 
# Hint: 1 ft is 0.3048 m. So we can get the output
#  in meters by multiplying the input distance
#  by 0.3048. Below is some sample input/output.

# referred to Talieson's b/c following sets is difficile


# main method/calculator
def convert(distance, conversion):
    result = distance * conversion
    print(f'The converted amount is {result} meters! ')


# starting value
no_exception = True
# initial purse/conversion
conversion = 0


    # take initial starting value (line 14)
user_input = input("what unit do you need converted? : ").strip().lower()

# fix unit to a standardized mode
if user_input in ["km", "kilometer", "kilometers"]:
    user_input == "km"
    conversion = 1000
    no_exception = False
elif user_input in ['f', 'feet', 'ft']:
    user_input == "feet"
    conversion = 0.3048
    no_exception = False
elif user_input in ['mi', 'miles', 'mile']:
    user_input = "mi"
    conversion = 1609.34
    no_exception = False
elif user_input in ['in', 'inches', 'inch', 'inchworm']:
    user_input == 'in'
    conversion = 0.0254
    no_exception = False
elif user_input in ['cm', 'centimeters', 'centimeter']:
    user_input == 'cm'
    conversion = 100
    no_exception = False
elif user_input in ['m', 'meters', 'meter']:
    user_input == 'm'
    conversion = 1
    no_exception = False
else:
    print(f'{user_input} is not a known measurement. Select something else')

# amount from user
distance = float(input("Enter distance to convert: "))

# check if it is a valid amount
while distance is float or int:
    break
else:
    print(f'{distance} is not a known number. Try again here: ')


convert(distance, conversion)