from ..calculator_math import mean, median, mode

# This lab allows the user to find the average of a set of numbers.
# Version 2 allows the user to input the list of numbers, rather then
# taking flat values.
# Version 3 adds median functionality.
# Version 4 adds mode functionality.

# definte global variables
run = True
list_finished = False
operation = False
nums_list = []

# main run loop
while run:
    # check if the user has input done, if not keep taking numbers.
    while not list_finished:
        # check that we've got the operation from the user.
        while operation not in ("mean", "median", "mode"):
            operation = input(
                "Do you want to find a mean, median or mode? "
                ).lower().strip()

        # take input from user
        num = input("Enter a num to add to series, enter done to proceed. ")
        # if that input is a number
        if num.isdigit():
            # make it an integer, put it in our list, and show what we've got
            num = int(num)
            nums_list.append(num)
            print(nums_list)
        # if the user enters done, lets move on
        elif num == "done":
            list_finished = True
        else:
            print("that is not a valid response.")

    # call the correction function depending on which operator they've picked
    if operation == "mean":
        print(mean(nums_list))
    elif operation == "mode":
        print(mode(nums_list))
    elif operation == "median":
        print(median(nums_list))

    run = False
    nums_list = []
    checkin = input("Do you want to operate on another list? (Y/N) ")
    if checkin == "Y":
        run = True
        list_finished = False
        operation = False
