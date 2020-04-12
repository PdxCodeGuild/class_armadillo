# PDX Code Guild Fullstack Course
# Lab 03 Grading
# Samuel Purdy
# 4/7/2020

# Imports the random module
import random

# Custom Module used to verify inputs when using input().
import verify

correct_inputs = ["Yes", "No"]

# Gets the input from the user.
def get_user_input():
    user_input = None

    # Checks to see if the integer is within the desired range or if it is a string. 
    # If any of these inputs are not correct, it will continue to ask the question until a correct input is given.
    while not verify.valid_input(user_input, against_range = True, range_low = 0, range_high = 100):
        user_input = input("What score did you get on your test? (Respond in whole number from 0-100) ")

    # Returns the input as an integer instead of a string.
    return int(user_input)

# Returns the letter grade string based on the integer given.
def print_letter_grade(int1):
    if int1 >= 90:
        return "A"
    elif int1 >= 80:
        return "B"
    elif int1 >= 70:
        return "C"
    elif int1 >= 60:
        return "D"
    else:
        return "F"


# Returns the modifier string based on the integer given.
def get_plus_or_minus(int1):

    # Uses Modulus to help determine if it's a "+" or "-"
    plus_or_minus = int1 % 10
    if int1 >= 60 and int1 <= 99:
        if plus_or_minus <= 3:
            return "-"
        elif plus_or_minus >= 7:
            return "+"
        elif int1 == 100:
            return "+"
        else:

            # Used if no operator is returned to avoid a None return
            return ""

    # Used if no operator is returned to avoid a None return
    else:
        return ""


# Prints the grade message based on the input.
def print_grade_message(int1):

    # Generates a random score for your rival.
    rival_score = random.randint(0, 100)

    # Creates the letter grade based on the integer given.
    letter_grade = print_letter_grade(grade) + get_plus_or_minus(grade)

    # Prints the appropriate message, based on the integer given.
    print(f"Your grade for the test is {letter_grade}!")
    if rival_score >= int1:
        print("Your Rival got a better grade than you!")
    elif rival_score == int1:
        print("Your Rival got the same score as you!")
    else:
        print("You got a better score than your Rival!")


grading = "Yes"

while grading == "Yes":
    # Gets the input from the user and assigns it to a variable.
    grade = get_user_input()

    # Prints the message based on the input from the user.
    print_grade_message(grade)
    grading = None
    # Checks to see if the user wants to check another grade.
    while not verify.valid_input(grading, correct_inputs, against_list = True, against_string = True):
        grading = input("Would you like to enter another grade? (Yes/No) ")
