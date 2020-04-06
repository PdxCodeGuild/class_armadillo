

import string
import random


def encrypt_file(input_path, output_path, encryptor):
    with open(input_path, 'r') as input_file:
        contents = input_file.read()
    encrypted_contents = encryptor.encrypt(contents)
    with open(output_path, 'w') as output_file:
        output_file.write(encrypted_contents)




# def make_rotn(n):
#     def rotn(text):
#         output = ''
#         for char in text:
#             if char in string.ascii_lowercase:
#                 index = string.ascii_lowercase.find(char)
#                 index += n
#                 index %= len(string.ascii_lowercase)
#                 output += string.ascii_lowercase[index]
#             else:
#                 output += char
#         return output
#     return rotn
#
#
# rotn = make_rotn(13)






class Scrambler:
    def __init__(self):
        pass

    def encrypt(self, text):
        text = list(text)
        random.shuffle(text)
        return ''.join(text)

class RotEncryptor:
    def __init__(self, n):
        self.n = n

    def encrypt(self, text):
        output = ''
        for char in text:
            if char in string.ascii_lowercase:
                index = string.ascii_lowercase.find(char)
                index += self.n
                index %= len(string.ascii_lowercase)
                output += string.ascii_lowercase[index]
            else:
                output += char
        return output



rot13 = RotEncryptor(13)
text = input('enter some text: ')
print(rot13.encrypt(text))

encrypt_file('white_horse.txt', 'white_horse_encrypted.txt', rot13)










