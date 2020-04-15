# convert numbers to units desired

# what are the units?

# feet
# meters

# ask the user for the number of units
# print out equivalent converted units

input("Can you convert distance in feet?")

# I want 8 meters to become ft. Tell me the equivalent
# distance __________m

#we do a dictionary b/c we want a KEY and a value
#whereas a list is singular values
# doorknob and KEY
def desiRocks(input_units):
    unit_lists = {
        'ft' : 0.3048,
        'm' : 1,
    }

user = float(input("What is the distance and units?"))
# float > int

# #12 feet
# "12 feet"
# .split()
# "12"
# "feet"

input_distance, input_units = user.split(' ')
input_distance = float(input_distance) # this converts it into a number instead of string
input_units = 
#"i'm a 2.5 ft, and I want to become a m"

#distance_feet = user*unit_lists[]