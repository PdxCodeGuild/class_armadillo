
# Lab 15 - user input is on line 15 # Allow the user to input the amount of rotation used in the encryption. (ROTN)

def rotn(text, num):
  output = ''

  for c in text:
    code = ord(c)
    if 97 <= code <= 122:
      code -= 97
      output += chr((code + num)%26 + 97)

  return output

print(rotn('some_code', 14))

# https://stackoverflow.com/questions/1185775/using-a-caesarian-cipher-on-a-string-of-text-in-python
# from string import lowercase, uppercase

# def caesar(text, key):
#     result = []
#     for c in text:
#         if c in lowercase:
#             idx = lowercase.index(c)
#             idx = (idx + key) % 26
#             result.append(lowercase[idx])
#         elif c in uppercase:
#             idx = uppercase.index(c)
#             idx = (idx + key) % 26
#             result.append(uppercase[idx])
#         else:
#             result.append(c)
#     return "".join(result)

# # v1 completed with matt 1452 on 16 APR 2020

# # prompts the user for a string, and encodes it with ROT13.
# #sally


# # def rot13(text): # define the function
# #   alphabet = 'abcdefghijklmnopqrstuvwxyz' # original_list
# #   rot_alphabet = alphabet[13:] + alphabet[:13] #changed_list
# #   for i in range(len(text)):
# #         #iterate through 'sally'
# #     print(i, end = ' ')
# #         #create index for alphabet AND rot_alphabet
# #     index = alphabet.index(text[i])
# #     #take the index and convert that
# #     print(f'Your string and original index in the unrotated alphabet is:  {text[i],index}')

# #   return text
  

# # user_input = input("What is the string? : ")

# # # INTENDED RESULTprint(rot13('hello')) # uryyb
# # print((rot13(user_input)))

