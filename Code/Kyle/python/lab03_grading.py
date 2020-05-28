# Instructions

#     Have the user enter a number representing the grade (0-100)
#     Convert the number grade to a letter grade
# Numeric Ranges
#     90-100: A
#     80-89: B
#     70-79: C
#     60-69: D
#     0-59: F

check_grade = True  
while check_grade:
    grade = (input('Please enter in a grade: '))
    if grade.isnumeric():
        numeric_grade = int(grade)
    else:
        print("I'm sorry but I don't recognize your entry. Please use non-negative, whole numeric scores only.")
        continue
    if numeric_grade > 100:
        print(f"{numeric_grade}! That's very good. Almost...too...good. ")
        print("Let's try that again - you can't score better than 100. ")
        continue
    elif numeric_grade < 0:
        print(f"{numeric_grade}...I'm not sure how you scored a negative answer.") 
        print("Let's try again, with a positive score this time. ")
        continue
    else:
        ones_digit = numeric_grade % 10
        modifier = ""
        if ones_digit > 6:
            modifier = "+"
        elif ones_digit >= 3 and ones_digit <= 6:
            modifier = ""
        else:
            modifier = "-"
        if numeric_grade == 100:
            print("A+")
        elif numeric_grade >= 90: # and numeric_grade <= 100:
            print(f'A{modifier}')
        elif numeric_grade >= 80: # and numeric_grade < 90:
            print(f'B{modifier}')
        elif numeric_grade >= 70: # and numeric_grade < 80:
            print(f'C{modifier}')
        elif numeric_grade >= 60: # and numeric_grade < 70:
            print(f'D{modifier}')       
        else:
            print("F")


    while True:
        affirmatives = ['yes', 'y', 'sure', 'okay', 'fine', 'why not?']
        negatives = ['no', 'n', 'nope', 'negative', 'definitely not', 'no way']
        try_again = input("Would you like to enter another grade? ").lower()
        if try_again in affirmatives:
            break
        elif try_again in negatives:
            print("Thank you for playing.")
            check_grade = False
            break
        else:
            print("That's not a valid answer. Please try again.")
            