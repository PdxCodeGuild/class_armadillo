import shlex


# Does the math. Everything becomes a meter then becomes final unit.
def meter_conversion(distance_amount,
                     conversion_method_value,
                     final_converstion_method_value):
    meter_distance = distance_amount * float(conversion_method_value)
    final_distance = meter_distance * float(final_converstion_method_value)
    rounded_final_distance = round(final_distance, 2)
    print(f"That is a total of {rounded_final_distance} {final_unit}.")


# Takes the input and makes it into a float
def get_float(get_distance_amount):
    while True:
        distance_amount = input(get_distance_amount)
        try:
            distance_amount = float(distance_amount)
            return distance_amount
        except ValueError:
            print("That is not a valid response.")


run = True
check_units = True

# Main run loop.
while run:
    # touples containing (name, * meter to make, and * to make a meter)
    # replace this with a dictionary that only uses 1 value
    units = [
        ("in", 0.0254, 39.3701),
        ("ft", 0.3048, 3.2808),
        ("yd", 0.9144, 1.0936),
        ("mi", 1609.34, 0.0006),
        ("mt", 1, 1),
        ("km", 1000, 0.001),
    ]

# Sets the values for name, and both conversion function values.
    while check_units:
        begin_unit = input('''
Please select the unit of measurement you want to use
Available unit: in, ft, yd, mi, mt, km. ''').strip().lower()

        final_unit = input('''
Please select the unit of measurement you want your input to become
Available unit: in, ft, yd, mi, mt, km. ''').strip().lower()

        if begin_unit in ["in", "i", "inches", "inch"]:
            begin_unit = units[0][0]
            conversion_method_value = units[0][1]
            final_converstion_method_value = units[0][2]
        elif begin_unit in ["f", "feet", "ft"]:
            begin_unit = units[1][0]
            conversion_method_value = units[1][1]
            final_converstion_method_value = units[1][2]
        elif begin_unit in ["yd", "y", "yard", "yards"]:
            begin_unit = units[2][0]
            conversion_method_value = units[2][1]
            final_converstion_method_value = units[2][2]
        elif begin_unit in ["mi", "miles", "mile"]:
            begin_unit = units[3][0]
            conversion_method_value = units[3][1]
            final_converstion_method_value = units[3][2]
        elif begin_unit in ["m", "mt", "meter", "meters"]:
            begin_unit = units[4][0]
            conversion_method_value = units[4][1]
            final_converstion_method_value = units[4][2]
        elif begin_unit in ["km", "kilo", "kilometers", "kilometer"]:
            begin_unit = units[5][0]
            conversion_method_value = units[5][1]
            final_converstion_method_value = units[5][2]
        if final_unit in ["in", "i", "inches", "inch"]:
            final_unit = units[0][0]
            final_converstion_method_value = units[0][2]
        elif final_unit in ["f", "feet", "ft"]:
            final_unit = units[1][0]
            final_converstion_method_value = units[1][2]
        elif final_unit in ["yd", "y", "yard", "yards"]:
            final_unit = units[2][0]
            final_converstion_method_value = units[2][2]
        elif final_unit in ["mi", "miles", "mile"]:
            final_unit = units[3][0]
            final_converstion_method_value = units[3][2]
        elif final_unit in ["m", "mt", "meter", "meters"]:
            final_unit = units[4][0]
            final_converstion_method_value = units[4][2]
        elif final_unit in ["km", "kilo", "kilometers", "kilometer"]:
            final_unit = units[5][0]
            final_converstion_method_value = units[5][2]

        # verifies input as valid distance type.
        if begin_unit and final_unit in ["in", "ft", "yd", "mi", "mt", "km"]:
            check_units = False
        else:
            print("please enter a valid response")

    # Takes input, makes it a float.
    distance_amount = get_float("Enter the distance in selected unit: ")

    # Run the function
    meter_conversion(distance_amount,
                     conversion_method_value,
                     final_converstion_method_value)

    # We're done - stop the loop.
    run = False

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
