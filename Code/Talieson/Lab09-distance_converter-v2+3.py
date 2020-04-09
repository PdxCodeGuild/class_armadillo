run = True
check_units = True
conversion_method_value = 0

while run:
    while check_units:
        unit = input('''
Please select the unit of measurement you want to use
Available unit: km, ft, mi. ''').strip().lower()

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

    distance_amount = float(input("Enter the distance in selected unit: "))
    while distance_amount is float or int:
        break
    else:
        print('please enter a number.')

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
