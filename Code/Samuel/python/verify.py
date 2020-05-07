# Verify is used to check inputs taken from the console against whatever parameters you give it.
import string

# These functions below print a message into the console to say that the input is incorrect, and it will usually say what is looking for as far as a response goes.
def print_not_numeric_message(input_value):
    print(f"The input value, {input_value} is not numeric. Please enter a number.")

def print_not_negative_message(input_value):
    print(f"The input value, {input_value} is not a negative number. Please enter a negative number.")

def print_not_positive_message(input_value):
    print(f"The input value, {input_value} is not a positive number. Please enter a positive number.")

def print_not_correct_message(input_value, against_var):
    print(f"The input value, {input_value} is not of the desired result. Please enter {against_var} in order to continue")

def print_not_in_list_message(input_value, against_var):
    print(f"The input value, {input_value} is not of the desired result within the list. Please enter any input from {against_var} in order to continue")

def print_not_in_range(input_value, range_low, range_high):
    print(f"The input value, {input_value} is not within range. Please enter another number within the range of {range_low} and {range_high}.")

# Checks to see if the input is a float.
# str1 = string input, usually gotten from input()
def check_if_numeric(str1):
    # for each character in the string given, loop
    for char in str1:
        if not char.isnumeric():
            if char != "." and char != "-":
                return False
    return True

# valid_input() checks to see if an input is of the correct type, and if it is the desired input based on a multitude of options.
# input_value is the variable holding the input from the user.
# against_var is what we are testing against. Default to None incase the user wants to test if the unit is of the desired type and/or is positive or negative.
# against_string is used to test if input_value is a string.
# against_float is used to test if input_value is a float.
# against_integer is used to test if input_value is an integer.
# against_list is used to test if input_value is within a certain list.
# against_range is used to test a specified range.
# range_low is the lowest point of the range.
# range_high is the highest point of the range.
# is_positive is used to test if input_value is positive or not.
# is_negative is used to test if input_value is negative or not.
# is_numeric is used to test if input_value is numeric or not.
def valid_input(input_value, against_var = None, against_string = False, against_float = False, against_integer = False, against_list = False, against_range = False, range_low = 0, range_high = 0, is_positive = False, is_negative = False, is_numeric = False):
    if input_value == None:
        return False
    if not against_list and against_var:

        if(type(against_var) == str and against_string):
            if(input_value.lower().strip() == against_var.lower().strip()):
                return True
            else:
                print_not_correct_message(input_value, against_var)
                return False

        if(type(against_var) == int and against_integer):
            if(check_if_numeric(input_value)):
                if(int(round(float(input_value))) == against_var):
                    return True
                else:
                    print_not_correct_message(input_value, against_var)
                    return False
            else:
                print_not_numeric_message(input_value)
                return False

        if(type(against_var) == float and against_float):
            if(check_if_numeric(input_value)):
                if float(input_value) == against_var:
                    return True 
                else:
                    print_not_correct_message(input_value, against_var)
                    return False
            else:
                print_not_numeric_message(input_value)
                return False

    elif is_positive:
        if(check_if_numeric(input_value)):
            if float(input_value) > 0:
                return True
            else:
                print_not_positive_message(input_value)
                return False
        else:
            print_not_numeric_message(input_value)
            return False

    elif is_negative:
        if(check_if_numeric(input_value)):
            if float(input_value) < 0:
                return True 
            else:
                print_not_negative_message(input_value)
                return False
        else:
            print_not_numeric_message(input_value)
            return False

    elif is_numeric:
        if check_if_numeric(input_value):
            return True  
        else:
            print_not_numeric_message(input_value)
            return False

    elif against_range:
        if check_if_numeric(input_value):
            if float(input_value) in range(range_low, range_high):
                return True 
            else:
                print_not_in_range(input_value, range_low, range_high)
                return False
        else:
            print_not_numeric_message(input_value)
            return False

    elif against_list:

        if(type(against_var[0]) == str and against_string):
            for val in range(len(against_var)):
                if(input_value.lower().strip() == against_var[val].lower().strip()):
                    return True
            print_not_in_list_message(input_value, against_var)
            return False

        if(type(against_var[0]) == int and against_integer):
            if(check_if_numeric(input_value)):
                for val in range(len(against_var)):
                    if(int(round(float(input_value))) == against_var[val]):
                        return True
                print_not_in_list_message(input_value, against_var)
                return False
            else:
                print_not_numeric_message(input_value)
                return False

        if(type(against_var[0]) == float and against_float):
            if(check_if_numeric(input_value)):
                for val in range(len(against_var)):
                    if float(input_value) == against_var[val]:
                        return True
                print_not_in_list_message(input_value, against_var)
                return False
            else:
                print_not_numeric_message(input_value)
                return False

    else:
        print(f"The input value, {input_value} is not of the desired result. Please enter another input in order to continue")
        return False

# Tests below

# strings = ["test", "test1", "test2"]
# floats = [3.9, 5.1, 4.0]
# ints = [3, 5, 4]

# print(valid_input("4", is_numeric = True)) # Returns True
# print(valid_input("f", is_numeric = True)) # Returns False

# print(valid_input("test", "test", against_string = True)) # Returns True
# print(valid_input("test", "test1", against_string = True)) # Returns False

# print(valid_input("1", 1, against_integer = True)) # Returns True
# print(valid_input("1", 2, against_integer = True)) # Returns False

# print(valid_input("1.0", 1.0, against_float= True)) # Returns True
# print(valid_input("1.0", 2.0, against_float = True)) # Returns False

# print(valid_input("4", is_positive= True)) # Returns True
# print(valid_input("f", is_positive= True)) # Returns False
# print(valid_input("-4", is_positive= True)) # Returns False

# print(valid_input("4", is_negative= True)) # Returns False
# print(valid_input("f", is_negative= True)) # Returns False
# print(valid_input("-4", is_negative= True)) # Returns True

# print(valid_input("5", against_range= True, range_low= 0, range_high= 10)) # Returns True
# print(valid_input("11", against_range= True, range_low= 0, range_high= 10)) # Returns False
# print(valid_input("-1", against_range= True, range_low= 0, range_high= 10)) # Returns False
# print(valid_input("f", against_range= True, range_low= 0, range_high= 10)) # Returns False

# print(valid_input("4", strings, against_string = True, against_list= True)) # Returns False
# print(valid_input("3.9", strings, against_string = True, against_list= True)) # Returns False
# print(valid_input("test2", strings, against_string = True, against_list= True)) # Returns True

# print(valid_input("4", ints, against_integer= True, against_list= True)) # Returns True
# print(valid_input("7.9", ints, against_integer = True, against_list= True)) # Returns False
# print(valid_input("test2", ints, against_integer = True, against_list= True)) # Returns False

# print(valid_input("7", floats, against_float = True, against_list= True)) # Returns False
# print(valid_input("3.9", floats, against_float = True, against_list= True)) # Returns True
# print(valid_input("test2", floats, against_float = True, against_list= True)) # Returns False