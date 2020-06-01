

units = {
    'ft': 0.3048,
    'm': 1,
    'mi': 1609.34,
    'km': 1000,
    'yd':  0.9144,
    'in': 0.0254,

}



num = int(input('what number do you want to convert?: '))
input_unit = input('what unit of measurement you want to convert from: ')
output_unit = input('what unit of measurement would you like to convert to: ')

conversion = num * units[input_unit] 
new_conversion = abs(conversion / units[output_unit])
result = f'{num} {input_unit} is equal to {new_conversion} {output_unit} '
print(result)


