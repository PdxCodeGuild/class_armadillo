#lab15-rot13-v1 sample by instructor:

# using two alphabet strings
def rot13_option1_v1(text):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  rot_alphabet = alphabet[13:] + alphabet[:13]
  # rot_alphabet = 'nopqrstuvwxyzabcdefghijklm'
  output = ''
  for char in text: # iterate over the characters in text
    index = alphabet.find(char) # find the index of the character in the alphabet
    rot_char = rot_alphabet[index] # find the corresponding rotated character
    output += rot_char
  return output

# using two alphabet strings, arbitrary rotation
def rot13_option1_v2(text, n=13):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  rot_alphabet = alphabet[n:] + alphabet[:n]
  print(rot_alphabet)
  # rot_alphabet = 'nopqrstuvwxyzabcdefghijklm'
  output = ''
  for char in text: # iterate over the characters in text
    index = alphabet.find(char) # find the index of the character in the alphabet
    rot_char = rot_alphabet[index] # find the corresponding rotated character
    output += rot_char
  return output


# this will work for -26 to 26
# print(rot13_option1_v2('hello', 1))


# using a single alphabet string
def rot13_option2_v2(text, n=13):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  output = ''
  for char in text: # iterate over the characters in text
    index = alphabet.find(char) # find the index of the character in the alphabet
    index += n
    index %= len(alphabet)
    output += alphabet[index]
  return output


# print(rot13_option2_v2('hello', 2600+13))


# a  b  c  d   ...
# 97 98 99 100 ...

# rotating by using ord and chr
def rot13_option3_v2(text, n=13):
  output = ''
  for char in text: # iterate over the characters in text
    index = ord(char) # find the index of the character in the ascii table
    index -= ord('a')
    index += n
    index %= 26
    index += ord('a')
    output += chr(index)
  return output


print(rot13_option3_v2('hello', -13))


# rotating by building up a dictionary
def rot13_option4_v2(text, n=13):

  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  rot_alpabet = alphabet[n:] + alphabet[:n]

  # build up a dictionary mapping characters to rotate characters
  rotator = {}
  for i in range(len(alphabet)):
    rotator[alphabet[i]] = rot_alpabet[i]
  # print(rotator)

  output = ''
  for char in text:
    output += rotator[char]
  
  return output

# this will work for -26 to 26
print(rot13_option4_v2('hello', 1))




# handling special characters by adding more characters to the alphabet
def rot13_option2_v3a(text, n=13):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  alphabet += alphabet.upper()
  alphabet += ' _*=~!@#$%^&()[]{}'
  output = ''
  for char in text: # iterate over the characters in text
    index = alphabet.find(char) # find the index of the character in the alphabet
    index += n
    index %= len(alphabet)
    output += alphabet[index]
  return output

output = rot13_option2_v3a('hello world!', 13)
print(output)
print(rot13_option2_v3a(output, -13))


# handle special characters by putting them directly in the output
def rot13_option2_v3b(text, n=13):
  alphabet = 'abcdefghijklmnopqrstuvwxyz'
  output = ''
  for char in text: # iterate over the characters in text
    index = alphabet.find(char) # find the index of the character in the alphabet
    if index == -1:
      output += char
    else:
      index += n
      index %= len(alphabet)
      output += alphabet[index]
  return output

output = rot13_option2_v3b('hello world!', 13)
print(output)
print(rot13_option2_v3b(output, -13))