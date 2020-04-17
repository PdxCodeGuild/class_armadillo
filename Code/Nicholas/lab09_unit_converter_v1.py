#this lab converts a user provided length in feet to meters

feet = float(input("Enter a length in feet to convert to meters: "))  #gets length in feet from user

meter = feet*0.3048  #feet to meters conversion

print(str(feet) + " ft is equal to " + str(meter) + "m")  #print a string that includes the conversion