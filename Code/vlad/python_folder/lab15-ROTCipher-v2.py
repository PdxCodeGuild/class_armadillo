# Lab 15: ROT Cipher Version 2
#Allow the user to input the amount of rotation used in the encryption. (ROTN)

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
index =    ['0','1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20','21','22','23','24','25']
rot13 =    ['n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m']
rotation = int(input('what is the rotation amount? '))
user_input = input('Enter any word: ')
word = ''
# print(alphabet.index('c'))
# print(rot13[4])
for letter in user_input: 
    x = (alphabet.index(letter) + rotation) % 26 #
    # print(alphabet[x])
    print(x)  
    word += alphabet[x]
    # print(index_letter)
    # print(rot13[index_letter])
print(word)