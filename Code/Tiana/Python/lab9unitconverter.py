#Lab 95 Unit Converter

#ask the user for the number of feet
#1ft is 0.3048
feet = int(input("Enter the number of feet? "))
feet_meters = feet * 0.3048

#print out the equivalent distance in meters.
print(f"The distance in feet is {feet}. ")
print(f"{feet} ft is {feet_meters} meters. ")


#version 2 allow the user to also enter the units

units = {
    "feet": 0.3048,
    "miles": 1609.34,
    "meters": 1,
    "kilometers": 1000
}
choice = input("What unit would you like to use feet, inches, yards, miles, meters or kilometers? ")

amount = int(input(f"How many {choice} would you like to convert? "))
units["yards"] = 0.9144
units["inches"] = 0.0254

while choice not in units:
    print("not a valid choice")
    choice = input("Try again! Enter a unit.")
    amount = int(input(f"How many {choice} would you like to convert? "))
   # print(f"{amount} {choice} is = ")


if choice == "feet":
        print(f"{amount} feet = {amount * units['feet']} meters. ")
elif choice == "miles":
    print(f"{amount} miles = {amount * units['miles']} meters. ")

elif choice == "meters":
    print(f"{amount} meters = {amount * units['meters']} meters. ")

elif choice == "kilometers":
     print(f"{amount} kilometers = {amount * units['kilometers']} meters.")

elif choice == "inches":
     print(f"{amount} inches = {amount * units['inches']} meters.")

elif choice == "yards":
     print(f"{amount} yards = {amount * units['yards']} meters.")