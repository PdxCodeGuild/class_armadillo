
# v2
#Allow the user to input the amount of 
# rotation used in the encryption. (ROTN)
def rotn(text, n):
# f(x) with two params
  ...
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    # what we are working with
    rot_alphabet = alphabet[n:] + alphabet[:n]
    # from v1
    cipher = ""
    # empty purse to concatenate to
    for char in text:
        # iterate over list
        index = alphabet.index(char)
        # above gets index
        new_rot += rot_alphabet[index]
        #create new var to rotate alphabet
        if char == -1:
            new_rot += char
    return new_char


print(rotn('hello', 13)) # uryyb
print(rotn('hello', 2)) # jgnnq
print(rotn('jgnnq', -2)) # hello

text = input('what is your text?')
n = int(input('what is the rotation amount? '))
print(rotn(text, n))


