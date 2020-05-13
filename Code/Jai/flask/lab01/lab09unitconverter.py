unit = {
    'ft': .3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': .9144,
    'in': .0254
}




num = int(input("what is the distance in meters7?: "))

measurement = input("what unit of measurement would you like to convert your number to?: ")

conversion = num * unit[measurement]


print(f'{conversion=}')




