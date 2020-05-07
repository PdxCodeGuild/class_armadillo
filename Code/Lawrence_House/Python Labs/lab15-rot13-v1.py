# Version 1

def rot13(text):
   alphabet = "abcdefghijklmnopqrstuvwxyz"    # String of characters
   output = ""   # Returned word
   for char in text:  #for each char in user given word
       output += alphabet[(alphabet.find(char)+13)%26]      # Adds each letter using .find to find char + ROT 13, then using modulus 26 to get back in range
   return output
    
print(rot13('hello'))
