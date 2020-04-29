# index = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26"]
# input_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y","z"]
# encrypted_characters = []
# user_input = input("Enter your password, and I'll encrypt it for you in a super-insecure cypher: ").lower().split()
# encrypted_word = ""


# for letter in user_input:
#     encrypted_letter = input_characters.index(char)
#     encrypted_word += encrypted_characters[encrypted_letter]
#     print(encrypted_letter)
#     print(encrypted_characters[encrypted_letter])
# print()

# while not user_input.isalpha():
#     print("Please, alphabet characters only. ")
#     user_input = input("Enter your password, and I'll encrypt it for you in a super-insecure cypher: ").lower().split()


## declaring variables used in this lab
letters = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
specials = "!@#$%^&*()"
split_alphabet = "abcdefghijklm01234!@#$%nopqrstuvwxyz56789^&*()"
reverse_split_alphabet = "nopqrstuvwxyz56789^&*()abcdefghijklm01234!@#$%"

user_input = ""
alphabet = ""
reverse_alphabet = ""
old_password = ""
new_password = ""


old_password = input("Enter your password, and I'll encrypt it for you in a super-insecure cypher: ").lower()
while not old_password.isalpha():
    print("\nI'm sorry, I don't recognize one or more of your entered characters.")
    print("Please enter only alphabet characters. ")
    old_password = input("Enter your password, and I'll encrypt it for you in a super-insecure cypher: ").lower()

alphabet = letters
reverse_alphabet = alphabet[13:] + alphabet[:13]
# print(f'The flipped alphabet is {reverse_alphabet}')

for char in old_password:
    index = alphabet.find(char)
    reverse_char = reverse_alphabet[index]
    new_password += reverse_char
print(new_password)


