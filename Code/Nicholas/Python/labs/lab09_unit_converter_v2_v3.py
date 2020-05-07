#This lab converts various units to meters

#dictionary with unit and meter conversion:
units = {
    "feet" : 0.3048,
    "ft" : 0.3048,
    "miles" : 1609.34,
    "mi" :1609.34,
    "meters" : 1,
    "m" : 1,                #various unit's equivalent to 1 meter
    "kilometers" : 1000,     
    "km" : 1000,
    "yards" : 0.9144,
    "yd" : 0.9144,
    "inches" : 0.0254,
    "in" : 0.0254
    }

unit = input("Please enter the unit you want converted to meters: ").lower()  #takes length
distance = float(input(f"Enter the length in {unit} that you want to convert to meters: "))  #asks for unit
#multiplies input distance times conversion factor from dictionary
result = distance * units[unit]  
print(f"{distance} {unit} is {result} meters")  #answer provided in formatted string