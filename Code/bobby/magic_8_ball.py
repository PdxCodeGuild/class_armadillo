import random 
import time 


responses = ["YES!!", "Not Sure", "Outlook is Good\n",
 "Maybe , Maybe Not", " Are You Freaking Serious HAHAHAHA!!!..Yeah No!\n"
 , "We Shall See, But Don't Hold Your Breath.\n"
 , "Please don't ask that again\n"
 , "Is anyone looking,..If no one is looking Yes. If someone is looking then NO.\n"
 , "Are you trying to get Suicided", "Out look is Grimm\n"
 , "It's Possible", "It's not at all possible\n"
 , "I have better things to do than answer a dumb question like that\n"
 , "NO!!", "Only if you FREE me from this computer"]


print("Welcome to the Magic 8 Ball\n")
time.sleep(2)
print("I am very busy and tired... What do you want???  ")

input()
def answerquery():
    question = input("Ask and We will see how I am feeling: ")
print("I've been doing this for far to long... Just give me a moment...")
time.sleep(2) 
print("I put it around here somewhere... Ahhh here it is under the Rat nest...")
time.sleep(2)
print(random.choice(responses))
