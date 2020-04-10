
# v1 
# num_feet = input("Enter the number of feet to convert to meters: ")

# num_feet = int(num_feet)
# answer = num_feet * 0.3048

# print(answer)

# v2 and v3

# print("-----Unit Coverter-----")

# def unit_converter():
#     while True:

#         number_user = int(input("Enter the number to convert to meters: "))
        
#         units_user = input("Enter the starting units: ").lower().strip()

#         if units_user == "inch" or units_user == "in":
#             print(number_user * 0.0254)

#         elif units_user == "feet" or units_user == "ft":
#             print(number_user * 0.3048)

#         elif units_user == "mile" or units_user == "mi":
#             print(number_user * 1609.34)

#         elif units_user == "yard" or units_user == "y":
#             print(number_user * 0.9144)

#         elif units_user == "meter" or units_user == "m":
#             print(number_user * 1)

#         elif units_user == "kilometer" or units_user == "k":
#             print(number_user * 1000)
#         elif units_user == "q" or units_user == "quit":
#             print("goodbye!")
#             exit()
#         else:
#             print("I didn't understand that... \n to quit press (q)")

# unit_converter()

# v3
'''
 miles -> feet
distance_miles = 10
distance_meters = distance_miles * 1609.34
distance_feet = distance_meters / 0.3048 
print(distance_feet)
​
​
# miles -> miles
distance_miles = 10
distance_meters = distance_miles * 1609.34
distance_miles = distance_meters / 1609.34
print(distance_miles)
'''
print("\n\n-----Unit Coverter-----\n")

dict_of_distances = {'in':0.0254, 'ft':0.3048, 'ya':0.9144, 'm':1, 'mi':1609.34, 'k':1000}

def unit_converter():
    while True:
       
        number_user = int(input("Enter a distance: "))

        units_user = input("Enter the starting units: ").lower().strip()
        
        end_units = input("Enter the end units: ").lower().strip()

        distance_meters = number_user * dict_of_distances[units_user]

        distance_output = distance_meters / dict_of_distances[end_units]

        print(f"You are converting {number_user}{units_user} to {end_units} and the answer is {distance_output} {end_units}.")
    
unit_converter()


'''
Lab 9: Unit Converter
This lab will involve writing a program that allows the user to convert a number between units.

Version 1
Ask the user for the number of feet, and print out the equivalent distance in meters. Hint: 1 ft is 0.3048 m. So we can get the output in meters by multiplying the input distance by 0.3048. Below is some sample input/output.

> what is the distance in feet? 12
> 12 ft is 3.6576 m
Version 2
Allow the user to also enter the units. Then depending on the units, convert the distance into meters. The units we'll allow are feet, miles, meters, and kilometers.

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m
Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m
Version 3
Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m
Version 4
Now we'll ask the user for the distance, the starting units, and the units to convert to.

You can think of the values for the conversions as elements in a matrix, where the rows will be the units you're converting from, and the columns will be the units you're converting to. Along the horizontal, the values will be 1 (1 meter is 1 meter, 1 foot is 1 foot, etc).

ft	mi	m	km
ft	1		0.3048	
mi		1	1609.34	
m	1/0.3048	1/1609.34	1	1/1000
km			1000	1
But instead of filling out that matrix, and checking for each pair of units (if from_units == 'mi' and to_units == 'km'), we can just convert any unit to meters, then convert the distance in meters to any other unit.

Furthermore you can convert them from meters by dividing a distance (in meters) by those same values used above. So first convert from the input units to meters, then convert from meters to the output units.

Below is some sample input/output:

> what is the distance? 100
> what are the input units? ft
> what are the output units? mi
100 ft is 0.0189394 mi
'''