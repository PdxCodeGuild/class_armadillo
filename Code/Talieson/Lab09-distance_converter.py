run = True

# Main run loop
while run:
    # Take input of feet and convert to a float
    distance_amount = float(input("Enter the distance in feet: "))
    # Multiply amount into yards
    distance_amount = (distance_amount * 0.3048)
    # Return answers
    print("That is a total of " + str(distance_amount) + " meters.")

    run = False

    # Quick check to see if there is more conversion to be done.
    while not run:
        go_again = input("Do you have more conversion to do? (Y/N) ")
        if go_again == "Y":
            run = True
            currency_check = True
            break
        if go_again == "N":
            exit()
        else:
            print("That is not a valid response.")
