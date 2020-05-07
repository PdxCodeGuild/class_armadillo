
#   Version 1

#user_distance = int(input('What is the distance in feet? '))

#print(user_distance * 0.3048)

#   Version 2 + 3 Unit to Meters

user_distance = int(input('What is the distance? '))

user_unit = input('What are the input units? ')

user_output = input('What are the output units? ')


if user_unit == "mi" or user_unit == "mile":
    meter_output = (user_distance * 1609.34)
elif user_unit == 'ft' or user_unit == 'feet':
    meter_output = (user_distance * 0.3048)
elif user_unit == 'km' or user_unit == 'kilometer':
    meter_output = (user_distance * 1000)
elif user_unit == 'm' or user_unit == 'meter':
    meter_output = (user_distance * 1)
elif user_unit == 'yd' or user_unit == 'yard':
    meter_output = (user_distance * 0.9144)
elif user_unit == 'in' or user_unit == 'inch':
    meter_output = (user_distance * 0.0254)

#print(meter_output)

#   Version 4 Full Unit Conversion

if user_output == "mi" or user_output == "mile":
    distance_output = (meter_output / 1609.34)
elif user_output == 'ft' or user_output == 'feet':
    distance_output = (meter_output / 0.3048)
elif user_output == 'km' or user_output == 'kilometer':
    distance_output = (meter_output / 1000)
elif user_output == 'm' or user_output == 'meter':
    distance_output = (meter_output / 1)
elif user_output == 'yd' or user_output == 'yard':
    distance_output = (meter_output / 0.9144)
elif user_output == 'in' or user_output == 'inch':
    distance_output = (meter_output / 0.0254)

print(f"{user_distance} {user_unit} is {distance_output} {user_output}")

#distance_miles = 10
#distance_meters = distance_miles * 1609.34
#distance_feet = distance_meters / 0.3048 

#print(distance_feet)

# miles -> miles

#distance_miles = 10
#distance_meters = distance_miles * 1609.34
#distance_miles = distance_meters / 1609.34

#print(distance_miles)

