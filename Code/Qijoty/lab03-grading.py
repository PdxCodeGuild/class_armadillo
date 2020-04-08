'''
print("hello")
print("Please enter a number representing the grade (0-100)")
num = int(input("Enter a number: "))


if num > 110:
    print("Oh wow, an A+!  You're a real scholar!")
elif num > 98:
    print("Wow, you are receiving an A!")
elif num > 94:
    print("The grade you are receiving is an A-, excellent!!")
elif num > 89:
    print("Great job, the grade you are receiving is a B+!")
elif num > 86:
    print("Alright, a B!")
elif num > 83:
    print("You are getting a B-, still okay.")
elif num > 79:
    print("The grade you are receiving is a C+, average.")
elif num > 76:
    print("You are receiving a C+")
elif num >73:
    print("You just barely made it to passing with a C-.")
elif num > 69:
    print("The grade you are receiving is a D+, yikes.")
elif num > 66:
    print("Oof, you are getting a D.")
elif num > 63:
    print("Dang, a D-...")
elif num > 59:
    print("F is for failure, did you even try?")
else:
    print("You are absolutely failing this class, maybe you should actually try next time...")
'''
#I'm not sure I understand the concatenate aspect
#here it is

print("hello")
print("Please enter a number representing the grade (0-100)")
while True:
    grade = input('Enter your grade: ')
    if gradeisnumeric():
        grade = int(grade)
        break
    print('That is not a valid number')

ones_digit = grade % 10
tens_digit = grade // 10
extra = ''
if ones_digit < 5:
    extra = '-'
if ones_digit > 5:
    extra = '+'

if grade >= 90:
    print('A' + extra)
elif grade >= 80:
    print('B' + extra)
elif grade >= 70:
    print('C' + extra)
elif grade >= 60:
    print('D' + extra)
elif grade >= 50:
    print('F' + extra)



num = int(input("Enter a number: "))

int(user_input)
user_grade % 10
if user_grade % 10 > 5:
    qualifier = '+'
elif user_grade % 10 == 5:
    qualifier = ''
elif user_grade % 10 < 5:
    qualifier = '-'
print(user_grade('qualifier'))

if num >= 90 and num <=100:
    print("You got an {num}{qualifier}!  You\'re quite the scholar!")


