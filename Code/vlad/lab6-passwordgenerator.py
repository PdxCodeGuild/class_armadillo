import random  # contain function and choices to randomaze 
import string  # contain function and choices to randomaze 

lower = string.ascii_lowercase  # the .dot will go inside the string module
upper = string.ascii_uppercase  # the .dot will go inside the string module

letters = string.ascii_letters

# print(lower + upper)
# print(letters)
# exit() this portion will stop the code here and wont allow anything below to run it can be used for testing the code

user = int(input("Enter a password length: "))  # you have to enter a number and then the generator will create a password for you. 
word = ""  # different way to write it word = str() 

#print(list(range(user)))

for i in range(user):
   #print(f"{i=}")  print the value of i for each iteration each that (pass through) the for loop
    word += random.choice(letters)  # other way to write this line is:  word = word + random.choice(letters)

print(word)
