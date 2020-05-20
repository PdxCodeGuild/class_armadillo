grade = int(input('Enter score:'))

plus_minus = grade % 10


if plus_minus < 5:
    plus_minus = '-'
elif plus_minus > 5:
    plus_minus = '+'
else:
    plus_minus = ''

if grade > 90:
    print(f'A{plus_minus}')
elif grade > 80 and grade <= 89:
    print(f'B{plus_minus}')
elif grade > 70 and grade <+ 79:
    print(f'C{plus_minus}')
elif grade > 60 and grade <= 69:
    print(f'D{plus_minus}')
elif grade < 59:
    print(f'Fail{plus_minus}')