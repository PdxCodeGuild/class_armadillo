
# Lab 9: Unit Converter



## Version 1

# Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by **multiplying the input distance by 0.3048**. Below is some sample input/output.


# dict to store key and value of ft and meters
distance = {

    'feet': 1,
    'meters': 0.3048,
}
# asking user for input and storing it in user_distance
user_distance = int(input("Enter distance in feet:\n "))

#user_distance gets mulitplied by the value stored in the key meters 
len_amount = user_distance * distance['meters']

# f sttrring to frint user input and the amout in meters
print(f'{user_distance} ft is {len_amount} meters')






# c_unit = input(f"Enter the unit to convert from {list}: ")

# num = num * units[c_unit]



# print(num + 'c_unit')
units = {
    'ft': .3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': .9144,
    'in': .0254
}
list = list(units.keys())