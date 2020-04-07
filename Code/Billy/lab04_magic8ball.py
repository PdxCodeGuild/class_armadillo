import random

print('*'*80)
print('Welcome to the Magic 8-Ball...where your fortune awaits!')
print('*'*80)

question = input("ASK MAGIC 8-BALL A QUESTION AND THEN BE AMAZED BY ITS REPLY: ")

answers = ["It is certain.", "It is decidedly so.", "Reply hazy, try again.", "Ask again later.", "Don't count on it.", "Outlook good.", "Very doubtful.", "Signs point to yes.", "Hell to the NO!", "100% Yes. Sike! Lol.", "No! What are you smoking?", "You bet!"]

random_answer = random.choice(answers)

print(random_answer)