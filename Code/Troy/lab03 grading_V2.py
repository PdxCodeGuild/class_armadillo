# Lab 03 Grading
# Troy Fitzgerald
# 

''' Version 2

Find the specific letter grade (A+, B-, etc). You can check for more specific ranges 
using if statements, or use modulus % to get the ones-digit to set another string to
'+', '-', or ' '. Then you can concatenate that string with your grade string.'''

'''Numeric Ranges:
90-100: A
80-89: B
70-79: C
60-69: D
0-59: F'''
#
num = input("Enter a number: ")

num = int(num)

if num >= 90 and num <= 100:
    print ("A, out-freaking-standing")
elif num >= 80 and num <= 89:
    print("B, good job, but could be better.")
elif num >= 70 and num <= 79:
    print("It's a C, and thanks for showing up.")
elif num >= 60 and num <= 69:
    print("D, try harder.")
elif num >= 0 and num <= 59:
    print("Then you get an F.  You failed and may God have mercy on your soul.")'''

