"""


Lab 9: Unit Converter

Version 2 ==================================================================

- Allow the user to also enter the units; feet, miles, meters, and 
  kilometers.
- Then depending on the units, convert the distance into meters. 

1 ft is 0.3048 m
1 mi is 1609.34 m
1 m is 1 m
1 km is 1000 m

Below is some sample input/output:

> what is the distance? 100
> what are the units? mi
> 100 mi is 160934 m

Version 3 ==================================================================

-Add support for yards, and inches.

1 yard is 0.9144 m
1 inch is 0.0254 m

"""

import time # time dalays are just my preferance


distances = {'feet': 0.3048, 'miles': 1609, 'kilometers': 1000, 'yards': 0.9144, 'inches': 0.0254}
#print(distances) 

print("Let's talk about converting a number between units... ")

time.sleep(1)
while True:

  # V2 - Allow the user to also enter the units; feet, miles, meters, and kilometers
  print("Which unit would you like to convert to meters? ") 

  time.sleep(1)
  units = input(str("Your options are feet, miles, kilometers, yards, or inches. Or enter done to quit ")).lower 

  time.sleep(1)
  print(f"You chose: {units}")

# V2 - Depending on the units, convert the distance into meters. 
  if units == 'feet' or 'ft':
    
    time.sleep(1)
    feet = float(input("What is the number of feet? "))

    meters = feet*0.3048

    time.sleep(1)
    print(f"{feet} feet is equivalent to {meters} meters. ")
    break

  elif units == 'miles' or 'mi':
    
    time.sleep(1)
    miles = float(input("What is the number of miles? "))

    meters = miles*1609.34

    time.sleep(1)
    print(f"{miles} miles are equivalent to {meters} meters. ")   
    break

  elif units == 'kilometers' or 'km':
    
    time.sleep(1)
    kilometers = float(input("What is the number of kilometers? "))

    meters = kilometers*1000

    time.sleep(1)
    print(f"{kilometers} kilometers are equivalent to {meters} meters. ")
    break

  elif units == 'yards' or 'yd':
    
    time.sleep(1)
    yards = float(input("What is the number of yards? "))

    meters = yards/1.0936

    time.sleep(1)
    print(f"{yards} yards are equivalent to {meters} meters. ")
    break

  # V3 - Add support for yards, and inches. 
  elif units == 'inches':
    
    time.sleep(1)
    inches = float(input("What is the number of inches? "))

    meters = inches/39.37

    time.sleep(1)
    print(f"{inches} inches are equivalent to {meters} meters. ")
    break

  elif units == 'exit' or 'done':

    time.sleep(1)
    print("Goodbye. ")
    break



