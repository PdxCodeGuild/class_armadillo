
# asks the user what distance is
user_distance= int(input('What is the distance? '))
# asks the user what unit of measurement they would like converted
user_input = input('What unit would you like to convert? ')
# asks the user what unit of measurement they would like the previous answer converted to 
user_output = input('What unit do you want it converted to? ')
# distance conversions chart
distance_conversions = {'inches': 0.0254,
                        'feet': 0.3048,
                        'yards': 0.9144,
                        'meters': 1,
                        'miles': 1609.34,
                        'kilometers': 1000
} 

# formula to convert one unit of measurement to another unit of measurement
total = user_distance * (distance_conversions[user_input]  /distance_conversions[user_output])
# prints the user output in the new unit of measurement
print(f"That is equal to...{total}.")