# V1
'''
def calculator():
    print("\n\n----- Simple Calculator -----\n")
    while True:
        opperator = input("\nwhat is the operation you'd like to perform or done to quit at anytime: ")
        if opperator == "done":
            print("Goodbye!")
            exit()
        first_num = input("\nWhat is the first number you'd like to math on: ")
        if first_num == "done":
            print("Goodbye!")
            exit()
        second_num = input("\nWhat is the second number you'd like to math on: ")
        if second_num == "done":
            print("Goodbye!")
            exit()

        # print(f"opperator = {opperator}")
        # print(f"first_num = {first_num}")
        # print(f"second_num = {second_num}")
        first_num = float(first_num)
        second_num = float(second_num)

        if opperator == "+":
            answer = first_num + second_num
            print(f"\n{first_num} {opperator} {second_num} = {answer} ")

        elif opperator == "-":
            answer = first_num - second_num
            print(f"\n{first_num} {opperator} {second_num} = {answer} ")

        elif opperator == "/":
            answer = first_num / second_num
            print(f"\n{first_num} {opperator} {second_num} = {answer} ")

        elif opperator == "*":
            answer = first_num * second_num
            print(f"\n{first_num} {opperator} {second_num} = {answer} ")

        else: 
            print("\nI don't understand that, try again... ")
        answer = answer 
        print (answer)
calculator()
'''

# V2
def calculator():
    print("\n\n----- Simple Calculator -----\n")
    while True:
        opperator = input("\nwhat is the operation you'd like to perform or done to quit at anytime: ")
        if opperator == "done":
            print("Goodbye!")
            exit()
        first_num = input("\nWhat is the first number you'd like to math on: ")
        if first_num == "done":
            print("Goodbye!")
            exit()
        second_num = input("\nWhat is the second number you'd like to math on: ")
        if second_num == "done":
            print("Goodbye!")
            exit()
            
        first_num = float(first_num)
        second_num = float(second_num)

        if opperator == "+":
            answer = first_num + second_num
            print(f"\n{first_num} {opperator} {second_num} = {answer} ")

        elif opperator == "-":
            answer = first_num - second_num
            print(f"\n{first_num} {opperator} {second_num} = {answer} ")

        elif opperator == "/":
            answer = first_num / second_num
            print(f"\n{first_num} {opperator} {second_num} = {answer} ")

        elif opperator == "*":
            answer = first_num * second_num
            print(f"\n{first_num} {opperator} {second_num} = {answer} ")

        else: 
            print("\nI don't understand that, try again... ")

        play_again = input("Would you like to keep doing math on this answer: y/n ")
        
        if play_again == "y":
            while True:
                answer = answer
                opperator_two = input("\nwhat is the operation you'd like to perform or done to quit at anytime: ")
                if opperator_two == "done":
                    print("Goodbye!")
                    exit()
                    
                third_num = input("\nWhat is the number you'd like to math on: ")
                if third_num == "done":
                    print("Goodbye!")
                    exit()
                
                third_num = float(third_num)
                if opperator_two == "+":
                    answer = answer + third_num
                    print(f"\n{answer} {opperator_two} {third_num} = {answer} ")

                elif opperator_two == "-":
                    answer = answer - third_num
                    print(f"\n{answer} {opperator_two} {third_num} = {answer} ")

                elif opperator_two == "/":
                    answer = answer / third_num
                    print(f"\n{answer} {opperator_two} {third_num} = {answer} ")

                elif opperator_two == "*":
                    answer = answer * third_num
                    print(f"\n{answer} {opperator_two} {third_num} = {answer} ")
                else: 
                    print("\nI don't understand that, try again... ")   
        else:
            pass
calculator()


'''
Lab 13: Simple Calculator
Version 1
Let's write a simple REPL (read evaluate print loop) calculator that can handle addition, subtraction, multiplication, and division. Ask the user for an operator and each operand. Don't forget that input returns a string, which you can convert to a float using float(user_input) where user_input is the string you got from input. Below is some sample input/output.

> what is the operation you'd like to perform? +
> what is the first number? 5
> what is the second number? 12
> 5 + 12 = 17
> what is the operation you'd like to perform? done
> goodbye!
Version 2
Allow the user to have a running value, each command will perform an operation on that number.

> what is the starting number? 34
> enter operation: + 10
> 44
> enter operation: * 3
> 132
Version 3 (optional)
Allow the user to write an expression, alternating numbers and operators. Evaluate the expression left-to-right.

> what is the expression? 5 + 6 * 2
> 22
Version 4 (optional)
Allow the user to write an expression, alternating numbers and operators. Follow the proper order of operations, evaluating first exponentiation, then multiplication and division, then addition and subtraction.

> what is the expression? 5 + 6 * 2
> 17
Version 5 (optional)
Allow the user to write an expression including parantheses.

> what is the expression? 5*(6 + 2)
> 40

'''