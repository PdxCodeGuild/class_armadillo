import random
import time

eyes = [":", ";", "=", "X", "B"] # lists with various parts, grouped appropriately for horizontal emoticons
nose = ["-", ">", "3"]
mouth = [")", "(", "o", "P", "D", "|"]

# print one letter at a time
welcome_msg = '\nWELCOME TO THE RANDOM EMOTICON GENERATOR!\n'
i = 0
while i < len(welcome_msg):
    print(welcome_msg[i], end='', flush=True)
    time.sleep(0.1)
    i += 1

time.sleep(1) # time delay 1 sec

random_eyes = random.choice(eyes) # randomly selects body part from specified list
random_nose = random.choice(nose)
random_mouth = random.choice(mouth)
print('\n' + random_eyes + random_nose + random_mouth + '\n')

'''
# Lab 5: Random Emoticon Generator

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