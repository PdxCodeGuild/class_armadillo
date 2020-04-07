  
# Lab 3: Grading
# Let's convert a number grade to a letter grade, using if and elif statements and comparisons.

# Concepts Covered
# input, print
raw_score = input("What did you get on your test?")
# type conversion (str to int)
digit_score = int(input)
# comparisons (< <= > >=)
if digit_score > 90 and digit_score <= 100:
    print("A")
elif digit_score > 80 and digit_score <= 89:
    print("B")
elif digit_score > 70 and digit_score <= 79:
    print("C")
elif digit_score > 60 and digit_score <= 69:
    print("D")
else:
    print("Please retake the test")

# if, elif, else
# Instructions
# Have the user enter a number representing the grade (0-100)
# Convert the number grade to a letter grade
# Numeric Ranges
# 90-100: A
# 80-89: B
# 70-79: C
# 60-69: D
# 0-59: F
# Version 2
# Find the specific letter grade (A+, B-, etc). You can check for more specific ranges using if statements, or use modulus % to get the ones-digit to set another string to '+', '-', or ' '. Then you can concatenate that string with your grade string.