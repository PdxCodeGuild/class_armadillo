# Dictionary holidng base numbers and phrases with no pattern
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
    12 : 'twelve',
    13 : 'thirteen',
    14 : 'fourteen',
    15 : 'fifteen',
}



print('Enter a number to convert to phrase.')
digits = int(input('>'))

if digits < 16: 
    print(phrase[digits]) # numbers under 16 accessed through dictionary
elif digits == 20:
    print('twenty')
elif digits == 30:
    print('thirty')
elif digits == 40:
    print('forty')
elif digits == 50:
    print('fifty')
elif digits == 60:
    print('sixty')
elif digits == 70:
    print('seventy')    
elif digits == 80:
    print('eighty') 
elif digits == 90:
    print('ninety')


elif digits > 15 and digits < 20:   # 16 - 19 use base number in dictionary + teen
        digits %= 10
        print(f'{phrase[digits]}teen')

# for 21 - 99 print first phrase then use second digit to access root number phrase
elif digits > 20 and digits < 30:
    print(f'twenty-{phrase[digits%10]}') 
elif digits > 30 and digits < 40:
    print(f'thirty-{phrase[digits%10]}')
elif digits > 40 and digits < 50:
    print(f'forty-{phrase[digits%10]}') 
elif digits > 50 and digits < 60:
    print(f'fifty-{phrase[digits%10]}')
elif digits > 60 and digits < 70:
    print(f'sixty-{phrase[digits%10]}')
elif digits > 70 and digits < 80:
    print(f'seventy-{phrase[digits%10]}')
elif digits > 80 and digits < 90:
    print(f'eighty-{phrase[digits%10]}')
elif digits > 90 and digits < 100:
    print(f'ninety-{phrase[digits%10]}')

   
    


