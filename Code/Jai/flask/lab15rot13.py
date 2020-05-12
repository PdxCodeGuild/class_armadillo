import string


def rot13():
    alphabet = string.ascii_lowercase
    rot_alphabet = string.ascii_lowercase[13:] + string.ascii_lowercase[:13] 
    output = '' # start with a blank output string
    text = input("enter a string?: ")
    for char in text:# iterate over the characters of 'text' (the parameter)
        index = alphabet.find(char)# use .find with alphabet to get the index of the character in the alphabet
        rot = rot_alphabet[index] # use that same index to find the corresponding letter in the rotated alphabet
        output += rot # add the rotated character to the output +=
    return output

    
  
print(rot13())