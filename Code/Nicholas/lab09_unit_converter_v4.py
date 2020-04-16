#this lab takes user length and units and converts it to another selected units

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
    another_entry = input("Would you like to convert another unit? Y/N ").lower()  #allows user to enter another unit to convert
    if another_entry == 'n':
        print("Good bye!")
        break




