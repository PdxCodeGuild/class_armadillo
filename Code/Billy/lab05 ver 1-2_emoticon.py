import random
import time

eyes = [":", ";", "=", "X", "B"]
nose = ["-", ">", "3"]
mouth = [")", "(", "o", "P", "D", "|"]

# print one letter at a time
welcome_msg = '\nWELCOME TO THE RANDOM EMOTICON GENERATOR!\n'
i = 0
while i < len(welcome_msg):
    print(welcome_msg[i], end='', flush=True)
    time.sleep(0.1)
    i += 1

time.sleep(1)

while True:
    question = input('\nWould you like to generate five random emoticons? ').lower().strip()
    if question == 'yes':
        for x in range(5):
            random_eyes = random.choice(eyes) 
            random_nose = random.choice(nose)
            random_mouth = random.choice(mouth)
            print('\n' + random_eyes + random_nose + random_mouth)
            time.sleep(1)
    elif question != 'yes':
        time.sleep(0.5)
        print ('\nGood bye!\n')
        break
        
            
            


'''
Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are :-D =^P and :\

Define a list of eyes
Define a list of noses
Define a list of mouths
Randomly pick a set of eyes
Randomly pick a nose
Randomly pick a mouth
Assemble and display the emoticon

Version 2:
Use a while loop to generate 5 emoticons.
'''