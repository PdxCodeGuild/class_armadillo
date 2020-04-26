#Lab 9 Unit Converter Version 2

#Allow the user to also enter the distance 
units = {
    "feet": 0.3048,
    "miles": 1609.34,
    "meters": 1,
    "kilometers": 1000,
    "yards": 0.9144,
    "inches": 0.0254
}

choice = input("What unit would you like to use feet, inches, yards, miles, meters or kilometers? ")

#Allow user to input how many of the units to convert
amount = int(input(f"How many {choice} would you like to convert? "))

#Give another try if user does not choose an option from the list
while choice not in units:
    print("not a valid choice")
    choice = input("Try again! Enter a unit.")
    amount = int(input(f"How many {choice} would you like to convert? "))


#Conversion of distances 
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