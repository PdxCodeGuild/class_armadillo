
#             0         1         2
# fruits = ['apples', 'bananas', 'pears',]
# print(fruits[0])

# fruits = {
#     0: 'apples',
#     1: 'bananas',
#     2: 'pears'
# }
# print(fruits[0])

# dictionary is a collection of key-value pairs
# fruit_prices = {
#     'apples': 1.0,
#     'bananas': 1.25,
#     'pears': 100,
# }
# print(fruit_prices['apples']) # 1.0


def validate_units(input_units):
    unit_lists = [
        ['ft', 'feet'],
        ['mi', 'miles', 'mile'],
        ['m', 'meters', 'meter'],
        ['km', 'kilometers', 'kilometer'],
        ['yd', 'yards', 'yard'],
        ['in', 'inchs', 'inch'],
        ['nm', 'nanometers'],
    ]
    for unit_list in unit_lists:
        if input_units in unit_list:
            return unit_list[0]
    return None

    # if input_units == 'feet' or input_units == 'ft' or input_units == 'foot':
    #     return 'ft'
    # elif input_units == 'miles' or input_units == 'mi' or input_units == 'mile':
    #     return 'mi'



conversion_factors = {
    'ft': 0.3048,
    'mi': 1609.34,
    'm': 1.0,
    'km': 1000.0,
    'yd': 0.9144,
    'in': 0.0254,
}

# _ = 5
# print(_)

# 3 feet in meters
# 45 kilometers to miles
distance_units = input('what is the distance and units? ')
input_distance, input_units, _, output_units = distance_units.split(' ')
input_distance = float(input_distance)
input_units = validate_units(input_units)
output_units = validate_units(output_units)
if input_units is None or output_units is None:
    print('invalid units')
    quit()
distance_meters = input_distance*conversion_factors[input_units]
output_distance = distance_meters/conversion_factors[output_units]
output_distance = round(output_distance, 4)
print(f'{input_distance} {input_units} is {output_distance} {output_units}')

