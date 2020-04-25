

def ask_distance():
    user_distance = (input("Enter distance :\n "))
    if not user_distance.isdigit():
        user_distance = input("You Must Enter A Number: ")
    else:
        user_distance = int(user_distance)


    units = {
        'ft': .3048,
        'mi': 1609.34,
        'm': 1,
        'km': 1000,
        'yd': .9144,    
        'in': .0254
    }

    list = units.keys()
    user_conversion = input(f'What unit would you like to convert from?: {list}\n ')

    c_unit = input(f'Enter the unit to convert to?: {list}\n ')


    total = user_distance * (units[user_conversion] / units[c_unit])
    print(f'{user_distance} {user_conversion} is {total} {c_unit}')
ask_distance()

while True:

    again = input("Would you like to enter a new distance? Type 'y' for yes or 'n' for no: ")

    if again == 'y':
        ask_distance()
        continue


    else:
        print("Goodbye")
        break

