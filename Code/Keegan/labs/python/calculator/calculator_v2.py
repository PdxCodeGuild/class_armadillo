from calculator_v1 import calculator

calc_on = True
calc_again = 'y'
start_num = ''
while calc_on:

    valid_operators = ['+', '-', '*', '/']

    while True:
        if start_num == '':
            start_num = input("Please enter your starting number: ")

            # if the user input contains letters, continue looping
            if start_num.isalpha(): 
                print("That's not a valid number.")
                continue
            
            # if user input has no letters,
            else:
                try:  # try to convert to a float
                    start_num = float(start_num)
                    break
                except ValueError: # if conversion fails, throw an error and repeat loop
                    print(f"Can't convert {start_num} to a float")
                    start_num = ''
                    continue
        else:
            break

    while calc_again == 'y':
        operation = input("\nPlease enter your desired operation (i.e. '+ 10'): ").replace(' ','')
        if operation.isalpha():
            print(f"Sorry, you can only enter numbers and the following operators: {', '.join(valid_operators)}.")
        
        # first character in operation should be an operator
        operator = operation[0]

        # if first character is not an operator, ask for operation again
        if operator not in valid_operators:
            print(f"\nThe first character you enter must one of the following: {', '.join(valid_operators)}")
            break

        # the operand is the rest of the string after the first character
        operand = operation[1:]

        # for each character in the operation string
        for char in operand:
            # if the character is a letter, repeat loop
            if char.isalpha():
                print(f"invalid char: {char}")
                break

            # if the character isn't a digit, repeat loop
            elif not char.isdigit():
                # if the extraneous character is in the valid operators list
                if char in valid_operators:
                    print(f"your operation can only contain one operator")
                else:
                    if char != '.':
                        # if the extraneous character is some other punctuation
                        print(f"{char} is not an arithmetic operator.")
                break
    
        # call the calculator function from v1 and store the result
        result = calculator(start_num, operand, operator)
        
        # print result to the user
        print(f"{start_num} {operator} {operand} = {result}")

        # reset value of start_num for further calculations
        start_num = result


        # while loop to see if the user wants to 
        # perform another calculation

        calc_again = input("\nWould you like to perform another operation? y/n: ")
        
        while calc_again.lower() not in ['y', 'n']:
            print("\nPlease enter a valid selection")
            calc_again = input("Would you like to perform another operation? y/n: ")


        if calc_again == 'y':
            continue
        elif calc_again == 'n': 
            print("\n Thanks for using the calculator! Goodbye!")
            calc_on = False
            break
