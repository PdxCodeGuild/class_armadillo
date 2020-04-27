"""

Lab 13: Simple Calculator ==============================================

Version 2 
- Allow the user to have a running value, each command will 
            perform an operation on that number.

"""

print("Hello world, it's me Simple Calculator! ")

# V2 - Allow the user to have a running value    
running_or_not = input("Would you to perform operations on a running value? ").lower 

if running_or_not == "yes" or "y":
    starting_num = input("What is the starting number? ")
    starting_num = float(starting_num)
        
    running_num = starting_num
    print(f"Starting number: {starting_num}")


    while True:
        operator = input("Enter an operator or type done to exit: ")

        if operator == "+":
            second_num = input("How much would you like to add? ")
            second_num = float(second_num)

            the_sum = running_num + second_num

            # for testing
            # print(type(the_sum))
            # print(type(running_num))
            # print(type(second_num))
            print(f"{running_num} + {second_num} = {the_sum}")

            running_num += second_num
            print(f"Running Number: {running_num}")


        elif operator == "-":
            second_num = input("How much would you like to subtract? ")
            second_num = float(second_num)

            the_difference = running_num - second_num

            print(f"{running_num} - {second_num} = {the_difference}")

            running_num -= second_num
            print(f"Running Number: {running_num} ")

                
        elif operator == "*":
            second_num = input("Multiply by how much? ")
            second_num = float(second_num)

            the_product = running_num * second_num

            print(f"{running_num} * {second_num} = {the_product}")

            running_num *= second_num
            print(f"Running Number: {running_num} ")

                    
        elif operator == "/":
            second_num = input("Divide by how much? ")
            second_num = float(second_num)

            the_result = running_num / second_num

            print(f"{running_num} / {second_num} = {the_result}")

            running_num /= second_num
            print(f"Running Number: {running_num} ")

        elif operator == "done":
            print("Goodbye. ")
            break
#V1 - still an option
elif running_or_not == "no" or "n":
    operator = input("What is the operation you'd like to perform? (+, - , *, /) ")

    first_num = input("What is the first number? ")
    first_num = float(first_num)

    second_num = input("What is the second number? ")
    second_num = float(second_num)

    if operator == "+":
        print(f"{first_num} + {second_num} = {first_num+second_num}")

    elif operator == "-":
        print(f"{first_num} - {second_num} = {first_num-second_num}")

    elif operator == "*":
        print(f"{first_num} * {second_num} = {first_num*second_num}")

    elif operator == "/":
        print(f"{first_num} / {second_num} = {first_num/second_num}")

    else:
        print("Something went wrong. Please, try again. ")
