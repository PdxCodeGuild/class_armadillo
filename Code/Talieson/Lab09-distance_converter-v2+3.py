# Version 2 added ability to pick unit to convert from.
# Version 3 added inches and yards.


run = True
check_units = True
conversion_method_value = 0

# Main run loop
while run:
    # Take user input of which unit they want to use
    while check_units:
        unit = input('''
Please select the unit of measurement you want to use
Available unit: in, ft, yd, mi, m, km. ''').strip().lower()

    # Check the inputed unit and set the way we'll generate the meters
    if unit in ["mi", "miles", "mile"]:
        unit == "mi"
        conversion_method_value = 1609.34
        check_units = False
    elif unit in ["f", "feet", "ft"]:
        unit == "ft"
        check_units = False
        conversion_method_value = 0.3048
    elif unit in ["km", "kilo", "kilometers", "kilometer"]:
        unit == "km"
        check_units = False
        conversion_method_value = 1000
    elif unit in ["yd", "y", "yard", "yards"]:
        unit == "yd"
        check_units = False
        conversion_method_value = 0.9144
    elif unit in ["in", "i", "inches", "inch"]:
        unit == "in"
        check_units = False
        conversion_method_value = 0.0254
    else:
        print("please enter a valid response")

    # Take the amount from the user
    distance_amount = float(input("Enter the distance in selected unit: "))

    # Ensure the input is a number
    while distance_amount is float or int:
        break
    else:
        print('please enter a number.')

    # Main conversion function
    def conversion(distance_amount, conversion_method_value):

        final_distance = distance_amount * conversion_method_value
        print(f"That is a total of {final_distance} meters.")

    conversion(distance_amount, conversion_method_value)
    run = False
    check_units = False

    # Quick check to see if there is more conversion to be done.
    while not run:
        go_again = input("Do you have more conversion to do? (Y/N) ")
        if go_again == "Y":
            run = True
            check_units = True
            break
        if go_again == "N":
            exit()
        else:
            print("That is not a valid response.")
