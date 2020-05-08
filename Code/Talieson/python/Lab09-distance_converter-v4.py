# Unit converter takes 1 distance unit and returns the value in another.
# Version 4 allows the user to pick an output unit. Previously just meters.


# Does the math. Everything becomes a meter then becomes final unit.
def meter_conversion(distance_amount,
                     conversion_factor,
                     final_converstion_factor):
    meter_distance = distance_amount * float(conversion_factor)
    final_distance = meter_distance * float(final_converstion_factor)
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


def validate_input(unit1, unit2, valid_inputs):
    if unit1 in valid_inputs and unit2 in valid_inputs:
        return False
    else:
        print("please enter a valid response")
        return True


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

        if begin_unit in ["in", "i", "inches", "inch", ]:
            begin_unit, conversion_factor = units[0][0], units[0][1]
        elif begin_unit in ["f", "feet", "ft", "foot", ]:
            begin_unit, conversion_factor = units[1][0], units[1][1]
        elif begin_unit in ["yd", "y", "yard", "yards", ]:
            begin_unit, conversion_factor = units[2][0], units[2][1]
        elif begin_unit in ["mi", "miles", "mile", ]:
            begin_unit, conversion_factor = units[3][0], units[3][1]
        elif begin_unit in ["m", "mt", "meter", "meters", ]:
            begin_unit, conversion_factor = units[4][0], units[4][1]
        elif begin_unit in ["km", "kilo", "kilometers", "kilometer", ]:
            begin_unit, conversion_factor = units[5][0], units[5][1]
        if final_unit in ["in", "i", "inches", "inch", ]:
            final_unit, final_converstion_factor = units[0][0], units[0][2]
        elif final_unit in ["f", "feet", "ft", ]:
            final_unit, final_converstion_factor = units[1][0], units[1][2]
        elif final_unit in ["yd", "y", "yard", "yards", ]:
            final_unit, final_converstion_factor = units[2][0], units[2][2]
        elif final_unit in ["mi", "miles", "mile", ]:
            final_unit, final_converstion_factor = units[3][0], units[3][2]
        elif final_unit in ["m", "mt", "meter", "meters", ]:
            final_unit, final_converstion_factor = units[4][0], units[4][2]
        elif final_unit in ["km", "kilo", "kilometers", "kilometer", ]:
            final_unit, final_converstion_factor = units[5][0], units[5][2]

    # Calls function to ensure the user inputs are valid distance types
        valid_units = ["in", "ft", "yd", "mi", "mt", "km"]
        check_units = validate_input(begin_unit, final_unit, valid_units)

    # Takes input, makes it a float.
    distance_amount = get_float("Enter the distance in selected unit: ")

    # Run the function
    meter_conversion(distance_amount,
                     conversion_factor,
                     final_converstion_factor,)

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
