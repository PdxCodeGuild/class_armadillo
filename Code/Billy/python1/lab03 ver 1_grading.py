while True:
    num_grade = input("Enter a number grade: ") # asks user for number grade
    if num_grade.isnumeric(): # checks to see if string input aboves is a number
        num_grade = int(num_grade) # if input is a number, converts it to an integer
        break # ends this loop if input is a number
    print('Invalid...is not numeric.') # enters this print line if above not satisfied due to not being a number then asks to enter number again

if num_grade >= 90: # prints below statement if number value criteria met then ends program 
    print("Letter grade: A")
elif num_grade >= 80:
    print("Letter grade: B")
elif num_grade >= 70:
    print("Letter grade: C")
elif num_grade >= 60:
    print("Letter grade: D")
else: 
    print("Letter grade: F")



'''
Lab 3: Grading

Let's convert a number grade to a letter grade, using `if` and `elif` statements and comparisons.

## Concepts Covered

- input, print
- type conversion (str to int)
- comparisons (< <= > >=)
- if, elif, else

## Instructions

1. Have the user enter a number representing the grade (0-100)
2. Convert the number grade to a letter grade

## Numeric Ranges

- 90-100: A
- 80-89: B
- 70-79: C
- 60-69: D
- 0-59: F


## Version 2

Find the specific letter grade (A+, B-, etc). 
You can check for more specific ranges using `if` statements, or use modulus `%` 
to get the ones-digit to set another string to `'+'`, `'-'`, or `' '`. 
Then you can concatenate that string with your grade string.   
'''  