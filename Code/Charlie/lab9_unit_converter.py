




units = {
    'ft': .3048,
    'mi': 1609.34,
    'm': 1,
    'km': 1000,
    'yd': .9144,
    'in': .0254
}

num = int(input("Enter distance in meters: "))
list = list(units.keys())

c_unit = input(f"Enter the unit to convert from {list}: ")

num = num * units[c_unit]



print(num + 'c_unit')