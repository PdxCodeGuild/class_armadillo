while True:
    num_grade = input("Enter a number grade: ") # asks user for number grade
    if num_grade.isnumeric(): # checks to see if string input aboves is a number
        num_grade = int(num_grade) # if input is a number, converts it to an integer
        break # ends this loop if input is a number
    print('Invalid...is not numeric.') # enters this print line if above not satisfied due to not being a number then asks to enter number again

sign_grade = num_grade % 10 # takes modulus to evaluate if grade is + or -
sign = ' ' # establishes sign variable, stays empty if modulus == 5 

if sign_grade > 5: # modulus greater than five indicates + grade
    sign = '+'
elif sign_grade < 5: # modulus less than five indicates + grade
    sign = '-'

if num_grade >= 90: # prints below statement if number value criteria met then ends program 
    print('Letter grade: A' + sign) # concatenates the sign value string determined above
elif num_grade >= 80:
    print('Letter grade: B' + sign)
elif num_grade >= 70:
    print('Letter grade: C' + sign)
elif num_grade >= 60:
    print('Letter grade: D' + sign)
else: 
    print('Letter grade: F') # no specific sign grade is given for 'F' grades

 


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