"""
Lab 3: Grading

Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

Concepts Covered
-input, print
-type conversion (str to int)
-comparisons (< <= > >=)
-if, elif, else

Instructions
1. Have the user enter a number representing the grade (0-100)
2. Convert the number grade to a letter grade

Numeric Ranges
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F
"""

grade = int(input('Please enter your number grade: '))

if grade >= 90:
    print("You got an A! ")
elif grade >= 80:
    print("You got a B. ")
elif grade >= 70:
    print("You got a C. ")
elif grade >= 60:
    print("You got a D. ")
elif grade < 60:
    print("You got an F. ")
