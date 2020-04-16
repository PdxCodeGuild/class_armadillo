# These are the string practice examples we did in class
# I tried to do them all using list comprehension or 
# the shortest solution possible

#  4/10/2020

def double_letters(word):
    '''
    Double every character in a string and return the result
    '''
    return ''.join([a*2 for a in word])

# print(double_letters("hello"))

def latest_letter(word):
    return sorted(word)[-1]

# print(latest_letter("pneumonoultramicroscopicsilicovolcanoconiosis"))

def count_letter(letter, word):
    '''
    Return the number of instances of a letter in a string
    '''
    return len([char for char in word if char == letter])

# print(count_letter("i", "pneumonoultramicroscopicsilicovolcanoconiosis"))
# print(count_letter("l", "hello"))

def print_powers_2(n):
    '''
    Print the powers of 2 where n is the exponent
    '''
    print(', '.join([str(2 ** i) for i in range(n)]))

