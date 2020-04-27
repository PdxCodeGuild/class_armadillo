# v1 completed with matt 1452 on 16 APR 2020

# prompts the user for a string, and encodes it with ROT13.
#sally


def rot13(text): # define the function
  alphabet = 'abcdefghijklmnopqrstuvwxyz' # original_list
  rot_alphabet = alphabet[13:] + alphabet[:13] #changed_list
  for i in range(len(text)):
        #iterate through 'sally'
    print(i, end = ' ')
        #create index for alphabet AND rot_alphabet
    index = alphabet.index(text[i])
    #take the index and convert that
    print(f'Your string and original index in the unrotated alphabet is:  {text[i],index}')

  return text
  

user_input = input("What is the string? : ")
# INTENDED RESULTprint(rot13('hello')) # uryyb
print(f'New index of your rotated string is: {rot13(user_input)}')

#for char in range NOT feasible
# use for char in text
# || for i in range(#)

# we want to make f(x) self-contained - we only want to operate 
# on parameters given, not on ones ousside the f(x)

# lines 19 and 21 should remain ousside b/c they shouldn't be
# used within the f(x)

#side effects, limits how reusable f(x) is if ousside

# input is shadowed beginning/end i.e. global vs local vars

# BELOW IS EXAMPLE OF HOW TO CALL A FUNCTION IN A PRINT LN
# def rotn(text, n):
#   text = input('what is your text?')
#   n = int(input('what is the roation amount?'))
# print(rotn(text, n))