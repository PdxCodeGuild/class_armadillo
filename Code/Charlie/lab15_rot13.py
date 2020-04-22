# version one


def rot13(text):
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    rot_alphabet = alphabet[13:] + alphabet[:13]
    output = ''
    for char in text:
        index = alphabet.find(char)
        rot_char = rot_alphabet[index]
        output += rot_char

    return output

# # version 2  
# def rotn(text, n=13):
#     alphabet ='abcdefghijklmnopqrstuvwxyz'
#     output = ''
#     for char in text:
#         index = alphabet.find(char)
#         index += n
#         index %= len(alphabet)
#         output += alphabet[index]

#     return output


# def rot13(text, n=13):
#     rotator = {}
#     alphabet ='abcdefghijklmnopqrstuvwxyz'
#     rot_alphabet = alphabet[n:] + alphabet[:n]
#     for i in range(len(alphabet)):
#         rotator[alphabet[i]] = rot_alphabet[i]
#         output = ''
#     return output
     

text = input('what is your text? ')

print(rot13(text))




