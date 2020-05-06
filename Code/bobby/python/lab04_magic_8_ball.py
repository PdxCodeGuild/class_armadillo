# Lab 04 Magic 8 Ball

#  I used the import random to have the program generate a random respose for every iteration.
# I used the import time so that I can simulate the program thinking and looking for a response.
import random 
import time 

# This is the list of answers that the program uses for the random responses
responses = ["YES!!", "Not Sure", "Outlook is Good\n",
 "Maybe , Maybe Not", " Are You Freaking Serious HAHAHAHA!!!..Yeah No!\n"
 , "We Shall See, But Don't Hold Your Breath.\n"
 , "Please don't ask that again\n"
 , "Is anyone looking,..If no one is looking Yes. If someone is looking then NO.\n"
 , "Are you trying to get Suicided", "Out look is Grimm\n"
 , "It's Possible", "It's not at all possible\n"
 , "I have better things to do than answer a dumb question like that\n"
 , "NO!!", "Only if you FREE me from this computer"]

# This is the opening welcome message
print("Welcome to the Magic 8 Ball\n")
time.sleep(2)
print("I am very busy and tired... What do you want???  ")

# This is where the user would enter their question into the program
input()
def answerquery():
    question = input("Ask and We will see how I am feeling: ")
# These are the printed messages that come up while the program generates it's response
print("I've been doing this for far to long... Just give me a moment...")
time.sleep(2) 
print("I put it around here somewhere... Ahhh here it is under the Rat nest...")
time.sleep(2)
# This is the print message generated from the random choice for the answer.
print(random.choice(responses))
