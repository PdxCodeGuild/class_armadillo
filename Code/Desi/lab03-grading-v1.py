# Lab 03

# mistakes caught: undefined variable, if/elif indentation
# 
# Have the user enter a number representing the grade (0-100)
# Convert the number grade to a letter grade
# 
letter_grade = int(input("Enter a number representing the grade (0-100): "))
print(letter_grade)

# The if..else statement evaluates test expression and 
# will execute the body of if only when the test condition 
# is True . If the condition is False , the body of else is 
# executed. Indentation is used to separate the blocks



if letter_grade >= 90 and letter_grade <= 100: 
    print("A Well done!")
elif letter_grade >= 80 and letter_grade <= 89: 
    print("B Good job!")
elif letter_grade >= 70 and letter_grade <= 79:
    print("C Not bad")
elif letter_grade >= 60 and letter_grade <= 69:
    print("D")
else:
    print("F")