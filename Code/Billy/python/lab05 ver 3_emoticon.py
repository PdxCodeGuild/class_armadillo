import random
import time

eyes = ["^", "-", "*", "'"] # lists with various parts, grouped appropriately for horizontal emoticons
mouth = ["_", "."]
head = [" ", "(", "[" ]

# print one letter at a time
welcome_msg = '\nWELCOME TO THE RANDOM EMOTICON GENERATOR!\n'
i = 0
while i < len(welcome_msg):
    print(welcome_msg[i], end='', flush=True)
    time.sleep(0.1)
    i += 1

time.sleep(1) # time delay 1 sec

while True: # loop to print five different emoticons until broken
    question = input('\nWould you like to generate five random vertical emoticons? (yes/no) ').lower().strip() # makes input lower case and removes any extra spaces before and after
    if question == 'yes':
        for x in range(5): # creates one emoticon at a time for five times before looping back up top to ask input again 
            random_head_1 = random.choice(head)
            random_eye= random.choice(eyes) # randomly selects body part from specified list
            random_mouth = random.choice(mouth)
            random_head_2 = " " # establishes head
            if random_head_1 == "(": # for symmetry, changes head based on random_head_1 selection
                random_head_2 = ")"
            elif random_head_1 == "[":
                random_head_2 = "]" 
            else:
                random_head_2 = " "  
            print('\n' + random_head_1 + random_eye + random_mouth + random_eye + random_head_2) # vertical face manufacture
            time.sleep(1)
    elif question != 'yes': # if answer to input is not yes, then good bye msg printed and program ends
        time.sleep(0.5)
        print ('\nGood bye!\n')
        break
        
            
            


'''
Lab 5: Random Emoticon Generator

Let's generate emoticons by assembling a randomly choosing a set of eyes, a nose, and a mouth. Examples of emoticons are `:-D` `=^P` and `:\`. You can view a long list on [wikipedia](https://en.wikipedia.org/wiki/List_of_emoticons).

1. Define a list of eyes
2. Define a list of noses
3. Define a list of mouths
4. Randomly pick a set of eyes
5. Randomly pick a nose
6. Randomly pick a mouth
7. Use concatenation to combine them and display the emoticon

Example output:
```
:-P
```

## Version 2

Use a `while` loop to generate 5 emoticons.

## Version 3

Randomly generate vertical emoticons like `^_^` `(-_-)`, `[*.*]`
'''