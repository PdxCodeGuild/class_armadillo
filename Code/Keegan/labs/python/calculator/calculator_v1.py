def calculator(operand1, operand2, operator):
    '''
    Take in two operands and an operator.
    Return the result of the operation.
    '''
    operand1 = float(operand1)
    operand2 = float(operand2)

    if operator == '+':
        result = operand1 + operand2
    elif operator == '-':
        result = operand1 - operand2
    elif operator == '*':
        result = operand1 * operand2
    elif operator == '/':
        result = operand1 / operand2
        

    
    return result


def main():
    calc_on = True
    while calc_on:
        valid_operators = ['+', '-', '*', '/']

        user_operator = input("\nPlease enter the operation you'd like to perform: ").replace(' ', '')

        while user_operator not in valid_operators:
                    
            user_operator = input(f"Sorry, that's not a valid operation.\n Please select one of the following: {', '.join(valid_operators)}: ")

        left_operand = input("Please enter the left operand: ")
        while left_operand.isalpha():
            left_operand = input("Your operands must be numbers!\nPlease enter the left operand : ")


        right_operand = input("Please enter the right operand: ")
        while right_operand.isalpha():
            right_operand = input("Your operands must be numbers!\nPlease enter the right operand : ")

        result = calculator(left_operand, right_operand, user_operator)
        print(f"\n{left_operand} {user_operator} {right_operand} = {result}")
        print("")

        calc_again = input("Would you like to perform another operation? y/n: ")
        while calc_again.lower() not in ['y', 'n']:
            print("\nPlease enter a valid selection")
            calc_again = input("Would you like to perform another operation? y/n: ")


        if calc_again == 'y':
            continue
        else: 
            print("\n Thanks for using the calculator! Goodbye!")
            calc_on = False

