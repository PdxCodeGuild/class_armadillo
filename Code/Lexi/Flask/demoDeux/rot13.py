def rot13(text):
    output = '' # makes empty output list
    for x in text: # iterates through input one character(chr)(char) at a time
        ascii_code = ord(x) # changes chr to ascii
        if 97 <= ascii_code <= 122: # lower case
            ascii_code -= 97 # starts sequence at 0
            output += chr((ascii_code + 13)%26 + 97) 
            # rotates, shifts, changes ascii to chr, adds to ouput variable
        else:
            output += chr(ascii_code)
            print(f'\n\'{x}\' is an invalid entry...cannot encrypt that character.') # input validation  
    return output

print(rot13('hello')) # uryyb
