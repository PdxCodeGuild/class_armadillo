# Version 2

def rotn(text, n):
    alphabet = "abcdefghijklmnopqrstuvwxyz"     # String of characters
    output = ""     # Returned word
    for char in text:       #for each char in user given word
        output += alphabet[(alphabet.find(char)+ n)%26]     # Adds each letter using .find to find char + user given ROT, then using modulus 26 to get back in range
    return output

print(rotn('hello', 14))