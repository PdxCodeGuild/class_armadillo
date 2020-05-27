# Lab 09 v4

#mistakes: misplaced operators
# wrote verbose kid initially
# referred to Talieson's and billy's

conv_rate = {"yd": .9144, "in" : .0254, "ft": .3048, "mi": 1609.34, "m": 1, "km": 1000, } 
    
user_dist = input("Please enter numeric distance: ") # user input
user_dist = float(user_dist) # converts to integer

entered = input("Please enter the units to convert to m (yd, in, ft, mi, m, km): ") # user input

desired = input("What unit do you want to convert to? 'yd', 'in', 'm', 'mi', 'ft': ")

new_amt = user_dist * (conv_rate.get(f"{desired}"))
print(f"\n{user_dist}{desired} equals {new_amt} {entered}")