"""
lab 13: rot 13
"""

# start with a blank output string
# loop through every character of the string that the user entered
# find the index of that character in the alphabet
# using that index, find the character in the rotated alphabet
# append that character to the output string


def rot13(text):

    alphabet         = 'abcdefghijklmnopqrstuvwxyz'
    alphabet_rotated = 'nopqrstuvwxyzabcdefghijklm'

    output = ''
    for char in text:
        index = alphabet.find(char)
        output += alphabet_rotated[index]
    return output


def rotn(text, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        index += n

        while index >= len(alphabet):
            index -= len(alphabet)

        #if index >= len(alphabet):
        #    index -= len(alphabet)
        output += alphabet[index]
    return output

# print(rotn('hello', 2))


# add support for non-letter characters
# use the modulus operator to wrap the index around
def rotn_v2(text, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        if index == -1:
            output += char
        else:
            index += n
            index %= len(alphabet)
            output += alphabet[index]
    return output

print(rotn_v2('hello world!', 13))


def rotn_v3(text, offset):
    output = ''
    for char in text:
        index = ord(char)
        if ord('a') <= index <= ord('z'):
            index -= ord('a')
            index += offset
            index %= ord('z') - ord('a') + 1
            output += chr(ord('a')+index)
        elif ord('A') <= index <= ord('Z'):
            index -= ord('A')
            index += offset
            index %= ord('Z') - ord('A') + 1
            output += chr(ord('A') + index)
        else:
            output += char

    print(output)


def min(a, b):
    return a if a < b else b
def max(a, b):
    return a if a > b else b
def clamp(a, b, v):
    if v < a:
        return a
    elif v > b:
        return b
    else:
        return v

def clamp(a, b, v):
    return a if v < a else b if v > b else v

clamp(0.0, 1.0, 0.76)






def rotn_v4(text, offset):
    return ''.join([chr(ord('a')+(ord(c)-ord('a')+offset)%26) if ord(c)>=ord('a') and ord(c)<=ord('z') else chr(ord('A')+(ord(c)-ord('A')+offset)%26) if ord(c)>=ord('A') and ord(c)<=ord('Z') else c for c in text])


