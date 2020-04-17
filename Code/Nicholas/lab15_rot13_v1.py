cipher = {'a':'n',    #dictionary that rotates each letter 13 places
          'b':'o', 
          'c':'p', 
          'd':'q', 
          'e':'r', 
          'f':'s', 
          'g':'t', 
          'h':'u', 
          'i':'v',
          'j':'w',
          'k':'x',
          'l':'y',
          'm':'z',
          'n':'a',
          'o':'b',
          'p':'c',
          'q':'d',
          'r':'e',
          's':'f',
          't':'g',
          'u':'h',
          'v':'i',
          'w':'j',
          'x':'k',
          'y':'l',
          'z':'m',
        }

def rot13(user_word, cipher):  #text and dictionary
    encryption = ''  #blank string
    for letter in user_word:  #scans through each letter in user's word
        if letter in cipher:
            encryption += cipher[letter]  #if user word contains characters in the rot13 dict, then add each respective letter to encrypt
        else:
            encryption += letter #otherwise just reproduces user input 'as is'
    return encryption  
user_word = input('enter a phrase to encrypt: ')  #requests word from user              
print(rot13(user_word, cipher))  # cycles user input through function