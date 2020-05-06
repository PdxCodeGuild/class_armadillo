def get_user_number():
    '''Small REPL that asks the user for a number and 
    ensures the number is an integer between 1 and 999'''
    
    while True:
        try:
            number = input("\nPlease enter a whole number 1-999 to convert to a phrase: ")
            int(number)

        except ValueError :
            print("Error. You must enter a number.")
            continue
        
        return int(number)
def get_digit(number, digit):
    '''return the specified digit of a number'''
    return number // digit

def to_roman_numerals(number):
    thousands = get_digit(number, 1000) * 1000
    hundreds = get_digit(number - thousands, 100) * 100
    tens = get_digit(number - thousands - hundreds, 10) * 10
    ones = number % 10 
    
    split_num = [thousands, hundreds, tens, ones]

    print(split_num)
    
    numeral = []       # numeral combo

    if number == 0:
        return numeral

    numerals = {
        1000 : {'char':'M','special':100,},
        500  : {'char':'D','special':100,},
        100  : {'char':'C','special':10,},
        50   : {'char':'L','special':10,},
        10   : {'char':'X','special':1,},
        5    : {'char':'V','special':1,},
        1    : {'char':'I','special':'',},
    }

    special_numerals = {
        4   : 'IV',
        9   : 'IX',
        40  : 'XL',
        90  : 'XC',
        400 : 'CD',
        900 : 'CM'  
    }
    numeral_keys = list(numerals.keys())

    
    # split the number into three digits
    # scale 

    for i in range(1, len(numeral_keys) + 1):
        divisor = numeral_keys[i - 1]
        quotient = number // divisor

        if quotient == 0:
            continue
        
        n = quotient * divisor

        print(f'\n{quotient = }\n{divisor = }\n{n = }')




def main():
    '''
    Main operation function
    '''
    number = get_user_number()
    # num_digits = split_num(number)

    result = to_roman_numerals(number)
    # print(f'{number}: {result}')

main()