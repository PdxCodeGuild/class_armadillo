#Lab 3 Grading

#Have the user enter a number representing the grade (0-100)

num_grade = int(input('Enter your number grade. '))

#Convert the number grade to a letter grade

ones_digit = (num_grade % 10)


if ones_digit >= 5:
    ones_digit = '+'
else:
   ones_digit = '-'

if num_grade >= 90 and num_grade <= 100:
    print(f"You got an A {ones_digit} !")
elif num_grade >= 80 and num_grade <= 89:
    print(f"You got a B {ones_digit} !")
elif num_grade >= 70 and num_grade <= 79:
    print(f"You got a C {ones_digit} !")
elif num_grade >= 60 and num_grade <= 69:
    print(f"You got a D {ones_digit} !")
elif num_grade >= 0 and num_grade <= 59:
    print(f"You got an F {ones_digit} !")
else:
    print(f"You did horrible!")


#ones_digit = (num_grade % 10)
#print(ones_digit)

