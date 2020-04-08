while True:
    num_grade = input("Enter a number grade: ")
    if num_grade.isnumeric():
        num_grade = int(num_grade)
        break
    print('Invalid...is not numeric.')

if num_grade >= 90:
    print("Letter grade: A")
elif num_grade >= 80:
    print("Letter grade: B")
elif num_grade >= 70:
    print("Letter grade: C")
elif num_grade >= 60:
    print("Letter grade: D")
else: 
    print("Letter grade: F")