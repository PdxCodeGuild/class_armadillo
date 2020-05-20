
distance = int(input(('Enter the distance:')))
input_unit = input('Enter units to convert from: ft, mi, m, km, yd, in:')
output_unit = input('Enter units to convert to: ft, mi, m, km, yd, in:')

conv_dict = {
    'ft': 0.3048,
    'mi': 1609.34,
    'km': 1000,
    'yd': 0.9144,
    'in': 0.0254,
    'm': 1
}



print(f'{distance} {input_unit} is equal to {distance * conv_dict[input_unit] / conv_dict[output_unit]} {output_unit}')

