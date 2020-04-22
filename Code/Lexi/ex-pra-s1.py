def set_lowercase(strings):
    newList = []
    for name in strings:
        newList.append(name.lower())
    print(newList)  


# WE CAN USE A FOR LOOP TO Convert input strings
#  to lowercase without any surrounding whitespace.


# OR

# # WE CAN USE A METHOD .lower()
# password = input("What's your password? ")
# password.encode()
# print(password)

txt = "welcome to the jungle"
print(txt)
x = txt.split()

print(x)