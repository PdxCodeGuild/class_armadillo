import random

print("Welcome to 8-ball")

# user name
name = input("Enter name:")

# lets user ask a question
question1 = input("Ask a Question: ")

#  possible answers for question
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

# assigned num to question1
num = (question1)


while num.isdigit():
    num = input("You must enter a valid question: ")
    
else:
    num = (question1)

while True:
    num = random.choice(answer)
    for i in range(1):
        print(num)
    question = input("Would you like to ask again?: ")
    if question in ["yes", "yeah", "sure", "ya"]:
            question1 = input("Ask a Question: ")
            num = random.choice(answer)
            for i in range(1):
                print(num)
                continue
    elif question not in ["yes", "yeah", "sure", "ya"]:

        print("Thanks for playing goodbye!!")
        break
