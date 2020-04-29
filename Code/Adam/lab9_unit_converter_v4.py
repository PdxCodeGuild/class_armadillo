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

