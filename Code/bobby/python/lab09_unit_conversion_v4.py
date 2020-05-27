import time
# My conversion Table.
rate_of_conversion = {
    'in': .0254,
    'ft': .3048,
    'yd': .9144,
    'mi': 1609.34,
    'm': 1,
    'km': 1000
    }

print('\nWelcome To Your Unit Converter V.4\n')
time.sleep(1)


while True:
    # User types in the distance they want to be converted
    user_input = float(input('Enter Distance to Convert: '))
    # User types in the Unit of messuerment they want to convert.
    unit_con = input('What Unit of Distance Would You Like to Convert:(in, ft, yd, mi, m, km: ')
    # This is to verify the users input.
    org_user = rate_of_conversion.get(unit_con, False)

    if org_user:
        m = user_input * (rate_of_conversion.get(f'{unit_con}'))
    # If user enters a wrong entry they will see this message    
    else:
        print(f'Your {unit_con} Does Not Compute')
        exit()

    # This is where the user will select the desired messurment they want to convert to.
    conv_to = input('\nSelect the unit you wish to convert to: in, ft, yd, mi, m, km: ')
    user_con = rate_of_conversion.get(conv_to, False)

    if user_con:
        dist = m / (rate_of_conversion.get(f'{conv_to}'))
        # Printing the Coversion.
        print(f'{user_input} {unit_con} = {dist} {conv_to}')

    cont = input('\n Would You Like a New Conversion? (y,n)')
    if cont != "y":
        time.sleep(1)
        print( 'Have a Nice Day')
        exit()
    