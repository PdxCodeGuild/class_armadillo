# # Exercise 9

# days = "Mon Tue Wed Thu Fri Sat Sun"
# months = "\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# print("Here are the days: ", days)
# print("Here are the months: ", months)

# print("""
# There's something going on here.
# With the three double-quotes.
# We'll be able to type as much as we like.
# Even 4 lines if we want, or 5, or 6.
# """)

# # Exercise 10

# tabby_cat = "\tI'm tabbed in. "
# persian_cat = "I'm split\non a line."
# backslash_cat = "I'm \\ a \\ cat. "

# fat_cat = """
# I'll do a list:
# \t* Cat food
# \t* Fishies
# \t* Catnip\n\t* Grass
# """
# print(tabby_cat)
# print(persian_cat)
# print(backslash_cat)
# print(fat_cat)

# #Exercise 11

# print("How old are you?", end = ' ')
# age = input()
# print("How tall are you?", end = ' ')
# height = input()
# print("How much do you weigh?", end=' ')
# weight = input()

# print(f"So you're {age} old, {height} tall and {weight} heavy.")

# #Exercise 12
# age = input("How old are you? ")
# height = input("How tall are you? ")
# weight = input("How much do you weigh? ")

# print(f"So you're {age} old, {height} tall and {weight} heavy.")

#Exercise 13

# from sys import argv
# script, first, second, third = argv

# print("This script is called:", script)
# print("Your first variable is:", first)
# print("Your second variable is:", second)
# print("Your third variable is:", third)

# Exercise 14

# from sys import argv
# script, user_name = argv
# prompt = '> '

# print(f"Hi {user_name}, I'm the {script} script.")
# print("I'd like to ask you a few questions. ")
# print("Do you like me {user_name}?")
# likes = input(prompt)

# print(f"Where do you live {user_name}?")
# lives = input(prompt)

# print("What kind of computer do you have?")
# computer = input(prompt)

# print(f"""
# Alright, so you said {likes} about liking me.
# You live in {lives}. Not sure where that is.
# And you have a {computer} computer. Nice.
# """)

# #Exercise 15 
# from sys import argv

# script, filename = argv
# txt = open(filename)

# print(f"Here's your file {filename}: ")
# print(txt.read())

# print("Type the filename again: ")
# file_again = input("> ")
# txt_again = open(file_again)
# orint(txt_again.read())

#Exercise 16

from sys import argv
script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1 : ")
line2 = input("line 2 : ")
line3 = input("line 3 : ")

print("I'm going to write these to the file. ")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close()