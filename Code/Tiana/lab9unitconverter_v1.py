#Lab 9 Unit Converter Version 1

#ask the user for the number of feet
#1ft is 0.3048
feet = int(input("Enter the number of feet? "))

#formula to convert to meters
feet_meters = feet * 0.3048

#rounding to the 3rd decimal place 
new_meters = round(feet_meters,3)

#print out the equivalent distance in meters.
print(f"The distance is {feet} feet. ")
print(f"{feet} ft is {new_meters} meters. ")


