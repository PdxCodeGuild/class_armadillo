


# lab 15 version 2

# with n= your saying to whatever letter is in the text to add hat ever n is equal to   
def rotn(text, n=13):
    alphabet ='abcdefghijklmnopqrstuvwxyz'
    output = ''
    for char in text:
        index = alphabet.find(char)
        index += n
        index %= len(alphabet)
        output += alphabet[index]

    return output
text = input('what is your text? ')

print(rotn(text, n=1))
