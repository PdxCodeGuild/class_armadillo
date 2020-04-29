# index = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
# input_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
# encrypted_characters = []
# user_input = input("Enter your password, and I'll encrypt it for you in a super-insecure cypher: ").lower().split()
# encrypted_word = ""


## declaring variables used in this lab
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
specials = "!@#$%^&*()"
split_alphabet = "abcdefghijklm01234!@#$%nopqrstuvwxyz56789^&*()"

reverse_split_alphabet = "nopqrstuvwxyz56789^&*()abcdefghijklm01234!@#$%"

split_alphabet_list = []
for i in split_alphabet:
    split_alphabet_list.append(i)


user_input = ""
alphabet = ""
reverse_alphabet = ""
old_password = ""
new_password = ""

print("\nWelcome to Lab 15: ROT Cipher\n")
print("In this second version, the user can select the number of rotation, 1-36\n")

# Version 1 code

# old_password = input("Enter your password, and I'll encrypt it for you in a super-insecure cypher: ").lower()

# alphabet = letters
# reverse_alphabet = alphabet[13:] + alphabet[:13]
# # print(f'The flipped alphabet is {reverse_alphabet}')

# for char in old_password:
#     index = alphabet.find(char)
#     reverse_char = reverse_alphabet[index]
#     new_password += reverse_char
# print(new_password)

def validate_input_function():  
    old_password2 = input("Enter your password, and I'll encrypt it for you in a super-insecure cypher: ").lower()
    for i in old_password2:
        while not i in split_alphabet_list:
            print("\nI'm sorry, I don't recognize one or more of your responses.")
            print("Please enter only alpha-numeric characters, or the following special characters: ")
            print("! @ # $ % ^ & * ( )\n")
            old_password2 = input("Enter your password, and I'll encrypt it for you in a super-insecure cypher: ").lower()
    return old_password2

def validate_rotation():
    x = input("Please enter a number to determine specific of low-grade 'cypher-protection': ")
    while not x.isnumeric():
        print("\nI don't understand your response. ")
        print("The non-negative number you select must be between 1 and 36. \n")
        x = input("Please enter a number to determine specific of low-grade 'cypher-protection': ")   
    # while not x.isnumeric() and not int(x) <= 36:
    #     print("\nYour request is outside the rotation range. ")
    #     print("The non-negative number you select must be between 1 and 36. \n")
    #     x = input("Please enter a number to determine specific of low-grade 'cypher-protection': ") 
    return x


def rot_v2(old_password2, x):
    new_password2 = ""
    #clean input of spaces
    #old_password2 = old_password2.split()
    #old_password2 = ''.join(old_password2)
    # check to see if user input passed as argument to function
    print(f'User\'s old password is: {old_password2}')
    #iterate over each character of old password
    for i in old_password2:
        new_password2 += split_alphabet[(split_alphabet.find(i) + x) % 36]
    # check 
    print(F'Internal end of function produces: {new_password2}')
    return new_password2


validate_input_function()
validate_rotation()
print(rot_v2(old_password2, x))