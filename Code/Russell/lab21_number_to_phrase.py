


phrase = {
    1 : 'one',
    2 : 'two',
    3 : 'three',
    4 : 'four',
    5 : 'five',
    6 : 'six',
    7 : 'seven',
    8 : 'eight',
    9 : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : 'twelve'

}
while True:
    print('Enter a number to convert to phrase.')
    digits = int(input('>'))

    if digits < 13: 
        print(phrase[digits])

    elif digits < 20:
        if digits == 13:
            print('thirteen')
        elif digits == 15:
            print('fifteen')
        else:
            digits %= 10
            print(f'{phrase[digits]}teen')
    elif digits < 99:
        if digits == 20:
            print('twenty')
        elif digits == 30:
            print('thirty')
        elif digits == 50:
            print('fifty')
        elif digits < 30:
            print(f'twenty-{phrase[digits%10]}') 
        elif digits >= 30 and digits <= 39:
            print(f'thirty-{phrase[digits%10]}') 
        elif digits >= 50 and digits <= 59:
            print(f'fifty-{phrase[digits%10]}')
    
    
        else:
            
            first_digit = digits // 10
            second_digit = digits % 10
            print(f'{phrase[first_digit]}ty-{phrase[second_digit]}')



