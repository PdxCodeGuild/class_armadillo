
# intro message.
print("#="*55)
print(''' Welcome to Calcutron - enter a 2 numbers and an operator seperated by a space to recieve an answer.
Currently exceptable operators are +, -, *, and /. ''')
print("#="*55)

# start main run loop.
run = True
while run:
    # take the input and split it into the 3 variables we'll need.
    first_number, operator, second_number = input("what is the operation you'd like to perform? ").split(" ")
    #convert both numbers to floats.
    first_number = float(first_number)
    second_number = float(second_number)
    # check which operator is needed and use the applicable arrithmatic.
    if operator == "+":
        result = first_number + second_number
    elif operator == "-":
        result = first_number - second_number
    elif operator == "*":
        result = first_number * second_number
    elif operator == "/":
        result = first_number / second_number

    # return the result.
    print(f"{first_number} {operator} {second_number} = {result}")

    # end the run and check if there is more to do.
    run = False
    while not run:
        repeat = input("Would you like to perform another operation? (Y/N) ")
        if repeat == "Y":
            run = True
            break
        if repeat == "N":
            print("Thanks for coming by!")
            exit()
        else:
            print("please enter a valid response")

