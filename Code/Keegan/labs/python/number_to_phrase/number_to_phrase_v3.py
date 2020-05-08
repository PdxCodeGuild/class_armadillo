    # num_places = [
    #     'quadrillion',
    #     'trillion',
    #     'billion',
    #     'million',
    #     'thousand'
    # ]
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

def to_roman_numerals(number):
    '''Given a number return the number as roman numerals'''

    numerals = {
        # 1000 : {'char':'M','special':'C',},
        # 500  : {'char':'D','special':'C',},
        100  : {'char':'C','special':10,},
        50   : {'char':'L','special':10,},
        10   : {'char':'X','special':1,},
        5    : {'char':'V','special':1,},
        1    : {'char':'I','special':'',},
    }
    numeral_keys = list(numerals.keys())


    print(f'{numeral_keys = }')

    top_lines = []       # lines above numerals denoting x1000
    numeral   = []       # numeral combo

    # final_numeral = [[],[]]
    for i in range(1, len(numeral_keys) + 1):
        divisor   = numeral_keys[i-1]  # current key in numerals dictionary
        
        quotient = number // divisor  # user's number floor divided by current key
        
        if quotient == 0:
            continue

        # handle x1000 lines above 3999
        if divisor == 1000:
            if quotient < 4:
                numeral.append(numerals[divisor]['char'] * quotient)

            else:
                while quotient > 3:
                    pass
                    #  = to_roman_numerals(quotient)

        prev_divisor = 0
        if 1 < i <= len(numeral_keys):
            prev_divisor = numeral_keys[i - 2]


        # print(f'{quotient * divisor = }, {divisor - prev_divisor = }')
        n = quotient * divisor
        if quotient * divisor == prev_divisor - divisor and n not in numeral_keys:
            curr_numeral = numerals[divisor]['char']
            prev_numeral = numerals[prev_divisor]['char']
            numeral.append(f"{prev_numeral}{curr_numeral}")
        else:
            numeral.append(f"{numerals[divisor]['char'] * quotient}")
        
        
        


    final_numeral = [top_lines, numeral]

    return final_numeral

# def get_thousands(number):
#     return number // 1000

# def get_hundreds(number):
#     '''return the hundreds digit of a number'''
#     return number // 100

# def get_tens(number):
#     '''return the tens digit of a number'''
#     return number // 10

# def get_ones(number):
#     '''return the ones digit of a number'''
#     return number % 10

# def split_num(number):
#     '''splits a number into hundreds, tens and ones digits.
#        returns digits as a list'''
    
#     hundreds = get_hundreds(number)
#     tens = get_tens(number - (hundreds * 100))
#     ones = get_ones(number - (tens * 10))

#     return [hundreds, tens, ones]

def main():
    '''
    Main operation function
    '''
    number = get_user_number()
    # num_digits = split_num(number)

    print(to_roman_numerals(number))


main()
