# This function adds two numbers
def addition(num1, num2):
    result = num1 + num2
    return result


# This function subtracts two numbers
def subtraction(num1, num2):
    result = num1 - num2
    return result


# This function multiplies two numbers
def multiplication(num1, num2):
    result = num1 * num2
    return result


# This function checks for division of 0 then divides two numbers
def division(num1, num2):
    if num1 == 0 or num2 == 0:
        print("You can't divide by 0!")
    else:
        result = num1 / num2
        return result
