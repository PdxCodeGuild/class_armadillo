# Lab 09 v4


another_conversion = True
while another_conversion:
    units = {
        "cm": 0.01,
        "centimeters": 0.01,
        "feet": 0.3048,
        "ft": 0.3048,
        "miles": 1609.34,
        "mi": 1609.34,
        "meters": 1,
        "m": 1,                
        "kilometers": 1000,
        "km": 1000,
        "yards": 0.9144,
        "yd": 0.9144,
        "inches": 0.0254,
        "in": 0.0254,
        }

    start = input("What unit are you converting?: ").lower()  #user enters unit
    amount = float(input(f"How much of '{start}' are ya talking about?: "))  #user enters length in chosen unit
    end = input(f"So {amount} {start} to what unit?: ").lower()  #user enters new unit to convert to

    converted = amount * units[start]  #converts user input to meters

    result = converted / units[end]  #converts meters to new unit

    print(f'{amount} {start} is equal to {result} {end}')  



# conv_rate = {"yd": .9144, "in" : .0254, "ft": .3048, "mi": 1609.34, "m": 1, "km": 1000, } 
    
# user_dist = input("Please enter numeric distance: ") # user input
# user_dist = float(user_dist) # converts to integer

# entered = input("Please enter the units to convert to m (yd, in, ft, mi, m, km): ") # user input

# desired = input("What unit do you want to convert to? 'yd', 'in', 'm', 'mi', 'ft': ")

# new_amt = user_dist * (conv_rate.get(f"{desired}"))
# print(f"\n{user_dist}{desired} equals {new_amt} {entered}")