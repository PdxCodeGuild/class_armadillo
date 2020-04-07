#  Nick Gallo
#  04/07/2020
#  Lab 003 - Grading

def grading_scale():
    
    checking_grade = True

    print("------Grading Scale------")
    
    while checking_grade == True:
        user_grade = input("Enter a number to find your grade out: ")
    

        while not user_grade.isnumeric():
            print("That's not a number.")
            user_grade = input("Enter a number to find your grade out: ")
            
        user_grade = int(user_grade)

        if user_grade >= 101:
            print("You're a genius!!")
        elif user_grade >= 90:
            print("You scored an A!")
        elif user_grade >= 80:
            print("You scored a B!")
        elif user_grade >= 70:
            print("You scored an C.")
        elif user_grade >= 60:
            print("You scored a D.")
        elif user_grade <= 59:
            print("You unfortunately failed this assignment. =[ ")      
        else:
            print("please try entering a valid number from 0 to 100.")
        
        while True:
            user_try_again = input("would you like to try again? y/n ")
            if user_try_again == "y":
                break
            elif user_try_again == "n":
                checking_grade = False
                print("Goodbye!")
                break
            else:
                print("Sorry, that's not a valid response.")
                continue

grading_scale()


'''
Lab 3: Grading
Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

Concepts Covered
input, print
type conversion (str to int)
comparisons (< <= > >=)
if, elif, else
Instructions
Have the user enter a number representing the grade (0-100)
Convert the number grade to a letter grade
Numeric Ranges
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
Version 2
Find the specific letter grade (A+, B-, etc). You can check for more specific ranges using if statements, or use modulus % to get the ones-digit to set another string to '+', '-', or ' '. Then you can concatenate that string with your grade string.
'''