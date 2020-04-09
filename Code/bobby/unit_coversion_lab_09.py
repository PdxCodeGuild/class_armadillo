import time

units = {
    "in": 0.0254,
    "ft": 0.3048,
    "yd": 0.9144,
    "mi": 1609.34,
    "m": 1,
    "km": 1000}
    
print("Welcome to the Unit Conveter \n")
time.sleep(2)
print("Please enter the distance, \n", 
"Then Unit of Disatance, \n", 
"Then Press Enter \ Return\n")
time.sleep(2)
print(
"in, \n"
"ft,\n"
"yd, \n"
"mi,\n"
"m,\n"
"km\n")

distance = int(input("Enter your distance/length: "))
unit = input("Enter the unit to convert from in, ft, yd, mi, m, km: ")
result = distance * units[unit]

print(f"There is {result} meters in {distance} {unit}(s)")
