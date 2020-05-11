def get_user_number():
    '''
    Small REPL that asks the user for a number and 
    ensures the number is an integer between 1 and 99
    '''
    while True:
        try:
            number = input("\nPlease enter a whole number 1-99 to convert to a phrase: ")
            int(number)
            if not 0 < int(number) < 100:
                raise ValueError

        except ValueError :
            print("Error. You must enter a number 1-99.")
            continue
        
        return int(number)

def number_to_phrase(split_num):
    '''
    Builds a phrase out of the number split into places,
    returns the complete phrase
    '''
    num_names = {
        0: {
            1: 'one',
            2: 'two',
            3: 'three',
            4: 'four',
            5: 'five',
            6: 'six',
            7: 'seven',
            8: 'eight',
            9: 'nine'
        },
        1: {
            1: 'eleven',
            2: 'twelve',
            3: 'thirteen',
            4: 'fourteen', 
            5: 'fifteen', 
            6: 'sixteen',
            7: 'seventeen',
            8: 'eighteen',
            9: 'nineteen'
        },
        2: 'twenty',
        3: 'thirty',
        4: 'fourty',
        5: 'fifty',
        6: 'sixty',
        7: 'seventy',
        8: 'eighty',
        9: 'ninety'
    }


    tens, ones = split_num

    phrase = ''
    if tens < 2:
        phrase += num_names[tens][ones]
    
    elif tens > 1:
        phrase += num_names[tens]
        if ones > 0:
            phrase += '-' + num_names[0][ones]
        
    return phrase

def get_tens(number):
    '''
    returns the tens digit of a number
    '''
    return number // 10

def get_ones(number):
    '''
    returns the ones digit of a number
    '''
    return number % 10


def main():
    '''
    Main operation function
    '''
    number = get_user_number()
    split_num = []

    tens = get_tens(number)
    split_num.append(tens)

    ones = get_ones(number - (tens * 10))
    split_num.append(ones)

    print(number_to_phrase(split_num))


main()
