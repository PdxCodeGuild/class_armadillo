# Lab 03 Grading
# Troy Fitzgerald
#


'''Let's convert a number grade to a letter grade, using if and elif statements and 
comparisons.

Instructions:

Have the user enter a number representing the grade (0-100)
Convert the number grade to a letter grade

Numeric Ranges
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F'''

# prompts the user to enter number grade.
num = input("Enter a number grade: ")
# changes the num string to an integer.
num = int(num)
# tests the number grade against the if/elif statements to print the appropriate response. 
if num >= 90 and num <= 100:
    print("A, great job. You get a gold star!")
elif num >= 80 and num <= 89:
    print("B, good job, but could be better.")
elif num >= 70 and num <= 79:
    print("It's a C, and thanks for showing up.")
elif num >= 60 and num <= 69:
    print("D, try harder.")
elif num >= 0 and num <= 59:
    print("You get an F.  You have failed and may God have mercy on your soul.")


