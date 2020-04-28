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
print((rot13(user_input)))