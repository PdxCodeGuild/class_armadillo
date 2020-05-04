"""
Lab 9: Unit Converter ============================================================

This lab will involve writing a program that allows the user to convert a 
number between units.

Version 4
- Ask the user for: the distance, the starting units, and the units to convert to.

Think of the values for the conversions as elements in a matrix, where the rows 
will be the units you're converting from, and the columns will be the units you're 
converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 
1 foot is 1 foot, etc).

    ft	        mi	        m	        km
----------------------------------------------
ft	1		                0.3048	
mi		        1	        1609.34	
m	1/0.3048	1/1609.34	1	        1/1000
km			                1000	    1

But nstead of filling out that matrix, and checking for each pair of units 
(if from_units == 'mi' and to_units == 'km'), we can just convert any unit to 
meters, then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters) 
by those same values used above. So first convert from the input units to meters, 
then convert from meters to the output units.

Below is some sample input/output:

> what is the distance? 100
> what are the input units? ft
> what are the output units? mi
100 ft is 0.0189394 mi

"""


# define a function that converts meters to a specified unit
# divide the distance in meters by the chosen units conversion factor
def m_to_unit(end_unit, distance): # the parameters will be distance and the end_unit
    if end_unit in ['feet','ft']:
        dist_in_ft = distance/0.3048
        print(f'{dist_in_ft} ft ')
    elif end_unit in ['miles','mile','mi']:
        dist_in_mi = distance/1609.34
        print(f'{dist_in_mi} mi ')
    elif end_unit in ['meters','meter','m']:
        dist_in_m = distance/1
        print(f'{dist_in_m} m ')
    elif end_unit in ['kilometers','kilometer','km']:
        dist_in_km = distance/1000
        print(f'{dist_in_km} km ')
# convert any unit to meters, then convert the distance in meters to any other unit


distance = input('What is the distance? ').strip() # ask for distance; remove any spaces
distance = float(distance) # convert distance to a float
print(distance) # for testing

# ask for starting unit; the start_unit
start_unit = input('What is the starting unit of measurement? ').lower().strip() # make a lowercase and strip spaces
print(start_unit) # for testing

# ask for unit to convert to to; the end_unit
end_unit = input(f'What unit of measurement are you converting {distance} {start_unit} to? ')
print(end_unit) # for testing

# convert the start_unit to meters then convert the distance in meters to any other unit
if start_unit in ['feet','ft']:
    dist_in_m = distance*0.3048 # 1 ft is 0.3048 m
    # print(dist_in_m) # testing
    m_to_unit(end_unit, dist_in_m)

elif start_unit in ['miles','mile','mi']:
    dist_in_m = distance*1609.34 # 1 mi is 1609.34 m
    # print(dist_in_m) # testing
    m_to_unit(end_unit, dist_in_m)

elif start_unit in ['meters','meter','m']:
    dist_in_m = distance*1 # 1 m is 1 m
    # print(dist_in_m) # testing
    m_to_unit(end_unit, dist_in_m)

elif start_unit in ['kilometers','kilometer','km']:
    dist_in_m = distance*1000 # 1 km is 1000 m
    # print(dist_in_m) # testing
    m_to_unit(end_unit, dist_in_m)
