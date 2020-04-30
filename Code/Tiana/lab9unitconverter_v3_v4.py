#Lab 9 Unit Converter Version 2


#allow the user to choose the units to be converted
units = {
    "feet": 0.3048,
    "miles": 1609.34,
    "meters": 1,
    "kilometers": 1000,
    "yards": 0.9144,
    "inches": 0.0254
}
#Ask for user input for which unit to start with
choice = input("What unit would you like to use feet, inches, yards, miles, meters or kilometers? ")
#Ask for user input to determine how many units to convert
amount = int(input(f"How many {choice} would you like to convert? "))


#Unit choices and conversions from meters to the unit chosen
if choice == "feet":
        print(f"{amount} feet = {amount * units['feet']} meters. ")
        meter_amount = amount * units['feet']

        meter_conv = round(meter_amount)/ 0.3048
        print(f"{round(meter_amount)} meters is = {round(meter_conv)} feet.")
       
elif choice == "miles":
    print(f"{amount} miles = {amount * units['miles']} meters. ")
  
    meter_amount = amount * units['miles']
    print(f" {meter_amount} meters = {meter_amount / 1609.34} miles ")


elif choice == "meters":
    print(f"{amount} meters = {amount * units['meters']} meters. ")
    meter_amount = amount * units['meters']
   

elif choice == "kilometers":
     print(f"{amount} kilometers = {amount * units['kilometers']} meters.")
     meter_amount = amount * units['kilometers']
     print(f" {meter_amount} meters = {meter_amount / 1000} kilometers")

elif choice == "inches":
     print(f"{amount} inches = {amount * units['inches']} meters.")
     meter_amount = amount * units['inches']
     print(f" {meter_amount} meters = {meter_amount / 0.0254} inches")

elif choice == "yards":
     print(f"{amount} yards = {amount * units['yards']} meters.")
     meter_amount = amount * units['yards']
     print(f" {meter_amount} meters = {meter_amount / 0.9144} yards")