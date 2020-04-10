#Version 1
# feet = float(input("Enter a length in feet to convert to meters: "))

# meter = feet*0.3048

# print(str(feet) + " ft is equal to " + str(meter) + "m")
# ---------------------------------------------------------------------------------------------
#Version 2/3

# units = {
#     "feet" : 0.3048,
#     "ft" : 0.3048,
#     "miles" : 1609.34,
#     "mi" :1609.34,
#     "meters" : 1,
#     "m" : 1,                #various unit's equivalent to 1 meter
#     "kilometers" : 1000,
#     "km" : 1000,
#     "yards" : 0.9144,
#     "yd" : 0.9144,
#     "inches" : 0.0254,
#     "in" : 0.0254
#     }

# unit = input("Please enter the unit you want converted to meters: ").lower()
# distance = float(input(f"Enter the length in {unit} that you want to convert to meters: "))

# result = distance * units[unit]
# print(f"{distance} {unit} is {result} meters")
# ---------------------------------------------------------------------------------------------

#Version 4 

another_conversion = True
while another_conversion:
    units = {
        "feet": 0.3048,
        "ft": 0.3048,
        "miles": 1609.34,
        "mi": 1609.34,
        "meters": 1,
        "m": 1,                #various units equivalent to 1 meter in dictionary
        "kilometers": 1000,
        "km": 1000,
        "yards": 0.9144,
        "yd": 0.9144,
        "inches": 0.0254,
        "in": 0.0254
        }

    unit_from = input("Please enter the unit you want to convert from: ").lower()  #user enters unit
    user_length = float(input(f"Enter the length in {unit_from} that you want to convert: "))  #user enters length in chosen unit
    unit_to = input(f"Please enter the new unit you want to convert {user_length} {unit_from} to: ").lower()  #user enters new unit to convert to

    distance_meters = user_length * units[unit_from]  #converts user input to meters

    new_length = distance_meters / units[unit_to]  #converts meters to new unit

    print(f'{user_length} {unit_from} is equal to {new_length} {unit_to}')
    another_entry = input("Would you like to convert another unit? Y/N ").lower()
    if another_entry == 'n':
        print("Good bye!")
        break




