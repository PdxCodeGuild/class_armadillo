
# v2
#Allow the user to input the amount of 
# rotation used in the encryption. (ROTN)
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
def rotn(text, n):
<<<<<<< HEAD
# f(x) with two params

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
=======
    # f(x) with two params
  ...
>>>>>>> 9a6434dc13637e21447ef13e4aa21adfce523995
    # what we are working with
    rot_chosen = alphabet[n:] + alphabet[:n]
    # from v1
    cipher = ""
    # empty purse to concatenate to
    for char in text:
        # iterate over list
        index = alphabet.index(char)
        # above gets index
<<<<<<< HEAD
        cipher += rot_alphabet[index]
        #create new var to rotate alphabet
        if char == -1:
            rot_alphabet += char
    return cipher
=======
        new_rot += rot_chosen[index]
        #create new var to rotate chosen
        if char == -1:
            new_rot += char
        else:
            index += n
            index %= len(alphabet)
    return new_char
>>>>>>> 9a6434dc13637e21447ef13e4aa21adfce523995


print(rotn('hello', 13)) # uryyb
print(rotn('hello', 2)) # jgnnq
print(rotn('jgnnq', -2)) # hello

text = input('what is your text?')
n = int(input('what is the rotation amount? '))
print(rotn(text, n))


