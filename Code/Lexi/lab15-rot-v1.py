# v1
# prompts the user for a string, and encodes it with ROT13.
user_input = input("What is the string? : ")
#sally

def rot13(input): # define the function
  alphabet = 'abcdefghijklmnopqrstuvwxyz' # original_list
  rot_alphabet = alphabet[13:] + alphabet[:13] #changed_list
  for char in range(len(user_input)):
        #iterate through 'sally'
    print(char, end = ' ')
        #create index for alphabet AND rot_alphabet
    index = alphabet.index(char)
    #take the index and convert that
    if char == index:

  return input
  

# INTENDED RESULTprint(rot13('hello')) # uryyb

