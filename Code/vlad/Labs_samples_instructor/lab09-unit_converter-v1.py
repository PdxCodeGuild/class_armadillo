#lab09-unit_converter-v1 sample by instructor: 

# import .helpers
# age = helpers.get_integer('please enter your age: ')
# num = helpers.get_float('please enter your distance: ')



# distance_feet = input('what is the distance in feet? ')
# distance_feet = float(distance_feet)
# distance_meters = distance_feet * 0.3048
# print(f'{distance_feet} feet is {distance_meters} meters')


def get_conversion_factor(units):
    if units in ['ft', 'feet']:
        return 0.3048
    elif units in ['mi', 'miles', 'mile']:
        return 1609.34
    elif units in ['m', 'meters', 'meter']:
        return 1
    elif units in ['km', 'kilometers', 'kilometer']:
        return 1000
    elif units in ['yd', 'yards', 'yard']:
        return 0.9144
    elif units in ['in', 'inchs', 'inch']:
        return 0.0254
    print('units not recognized')
    return None

# fruits = ['apples', 'bananas']
# a, b = fruits
# a = fruits[0]
# b = fruits[1]





# distance_units = input('what is the distance and units? ') # 3 feet
# input_distance, input_units = distance_units.split(' ')
# input_distance = float(input_distance)
# cf = 0
# if units in ['ft', 'feet']:
#     cf = 0.3048
# elif units in ['mi', 'miles', 'mile']:
#     cf = 1609.34
# elif units in ['m', 'meters', 'meter']:
#     cf = 1
# elif units in ['km', 'kilometers', 'kilometer']:
#     cf = 1000
# elif units in ['yd', 'yards', 'yard']:
#     cf = 0.9144
# elif units in ['in', 'inchs', 'inch']:
#     cf = 0.0254
# output_distance = input_distance*cf
# print(f'{input_distance} {input_units} is {output_distance} meters')



distance_units = input('what is the distance and units? ') # 3 feet
input_distance, input_units = distance_units.split(' ')
input_distance = float(input_distance)
cf = get_conversion_factor(input_units)
output_distance = input_distance*cf
print(f'{input_distance} {input_units} is {output_distance} meters')