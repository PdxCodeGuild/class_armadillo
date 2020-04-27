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

# prompts the user to enter number grade.
num = input("Please enter a number grade: ")
# changes the num string to an integer.
num = int(num)

# tests the number grade against the if/elif statements to print the appropriate response. 
if num >= 98 and num <= 100:
    print ("A+, out-freaking-standing!")
elif num >= 94 and num <= 97:
    print ("A, good job.")
elif num >= 90 and num <= 93:
    print ("A-, keep it up.")
elif num >= 87 and num <= 89:
     print("B+, not too shabby.")
elif num >= 84 and num <= 86:
     print("B, good job.")
elif num >= 80 and num <= 83:
     print("B-, keep it up.")
elif num >= 78 and num <= 79:
    print("It's a C+, gotta do better than that")
elif num >= 75 and num <= 77:
    print("It's a C, you've got work to do.")  
elif num >= 70 and num <= 74:
    print("It's a C-, walking a fine line.") 
elif num >= 60 and num <= 69:
    print("It's a D+, thanks for showing up.")
elif num >= 60 and num <= 69:
    print("It's a D, thanks for showing up.")
elif num >= 60 and num <= 69:
    print("It's a D-, thanks for showing up.")
elif num >= 0 and num <= 59:
    print("It's an F.  You failed and may God have mercy on your soul.")

