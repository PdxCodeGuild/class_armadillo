import random

# Lab 4: Magic 8-Ball


print("=======================")
print("WELCOME TO MAGIC 8-BALL")
print("=======================")
print("")
print("")
# user name
name = input("Please Enter Your Name: ")
print("")
print("")


# lets user ask a question
def ask_question():
    question1 = input(f"Hi {name}, Ask A Question: ")
    # if user input is a numer its invalid 
    if question1.isdigit():
        question1 = input("You must enter a valid question: ")
    else:
        print(random.choice(answer))
        
answer = ["It is certain",
 "It may be so",
 "Without a doubt",
 "Yes - definitely",
 "You can bet on it",
 "As I see it, yes",
 "Most likely",
 "Chances are good",
 "Yes", "I think so",
 "Not sure, try again",
 "Ask again later",
 "Better not tell you now",
 "Cannot predict now",
 "Concentrate and ask again",
 "Don't count on it",
 "No",
 "My sources say no",
 "Don't think so",
 "Very doubtful"]

ask_question()



while True:
    question = input("Would you like to ask again?: ")
    if question in ["yes", "yeah", "sure", "ya", "y"]:
            question = input("Ask Away: ")
            print(random.choice(answer))
            continue


    else:
        print("Thanks for playing goodbye!!")
        break
    

