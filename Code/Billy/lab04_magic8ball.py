import random
import time

answers = ["It is certain.", "It is decidedly so.", "Reply hazy, try again.", "Ask again later.", "Don't count on it.", "Outlook good.", "Very doubtful.", "Signs point to yes.", "Hell to the NO!", "100% Yes. Sike! Lol.", "No! What are you smoking?", "You bet!"]

print('\n' + '*'*80)
print('Welcome to the Magic 8-Ball...where your fortune awaits!')
print('*'*80)

time.sleep(1.5)

while True:
    question = input('\n' + 'ASK MAGIC 8-BALL A QUESTION AND THEN BE AMAZED BY ITS REPLY: ')
    random_answer = random.choice(answers)
    time.sleep(2)
    print('\n' + random_answer + '\n')
    time.sleep(1.5)
    next_question = input('Would you like to ask another question? (yes/no) ').lower().strip()
    if next_question != 'yes':
        print('\nOK! Bye!\n')
        break



