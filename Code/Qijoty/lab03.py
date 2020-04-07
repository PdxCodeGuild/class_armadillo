import random
import string

animal = input("Enter an animal: ")
water = input("Enter a body of water: ")
creature = input("Enter a mythical creature: ")
boat = input("Enter a type of boat: ")
bodypart = input("Enter a body part: ")
animaltwo = input("Enter a second animal: ")
clothingone = input("Enter an article of clothing: ")
clothingtwo = input("Enter a second article of clothing: ")
clothingthree = input("Enter a third article of clothing: ")
clothingfour = input("Enter a fourth article of clothing: ")
flower = input("Enter a flower: ")
verb = input("Enter a verb: ")

clothing = [clothingone, clothingtwo, clothingthree, clothingfour]
random.shuffle(clothing)

print(f"I started early, took my {animal},")
print(f"And visited the {water};")
print(f"The {creature} in the basement")
print(f"Came out to look at me.")

print(f"And the {boat} in the upper floor")
print(f"Extended hempen {bodypart},")
print(f"Presuming me to be a {animaltwo}")
print(f"Aground, upon the sands.")

print(f"But no man moved me till the tide")
print(f"Went past my simple {clothing[0]},")
print(f"And past my {clothing[1]} and my {clothing[2]},")
print(f"And past my {clothing[3]} too,")

print(f"And made as he would {verb} me up")
print("As wholly as a dew")
print(f"Upon a {flower}’s sleeve –")
print(f"And then I started too.")


#read eval print loop  'repl'
#ask a question, get an answer, use a while loop to repeat code based on input
affirmative = ['yes', 'y', 'sure', 'okay']
user_choice = input("Do you want to continue?")

while user_choice.lower() in affirmative:
    print("TOIGHT, lets mAdLiB!!!")
    user_choice = input("Do you want to try again?")
else:
      print("Thank you for playing!")  


#adjectives = input('Enter two adjectives)
#adjectives = adjectives.split(,)
#adjective1= adjectives[0]
#adjective2 = adjectives[1]

#or
#adjective1, adjective2 = input('Enter two adjectives separated by comma: ').split(',)
#)
#fruit1, fruit2 = ['apples' , 'bananas']


'''
random:
random.shuffle(adjectives)
adjective1, adjective2 = adjectives

or 

adjectives = input('Enter four adjectives: ').split (',')

adjective1 = random.choice(adjectives)
adjective2 = random.choice(adjectives)