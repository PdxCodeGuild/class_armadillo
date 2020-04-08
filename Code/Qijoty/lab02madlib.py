import random
import string

i = 0
while i < 1:
    
    animal = input("Enter an animal: ")
    water = input("Enter a body of water: ")
    creature = input("Enter a mythical creature: ")
    boat = input("Enter a type of boat: ")
    bodypart = input("Enter a body part: ")
    animaltwo = input("Enter a second animal: ")
    clothing = input("Enter an article of clothing: ")
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
    print(f"Aground, upon the sands.")
    print(f"But no man moved me till the tide")
    print(f"Went past my simple {clothing},")
    print(f"And past my {clothingtwo} and my {clothingthree},")
    print(f"And past my {clothingfour} too,")
    print(f"Went past my simple {clothing[0]},")
    print(f"And past my {clothing[1]} and my {clothing[2]},")
    print(f"And past my {clothing[3]} too,")

    print(f"And made as he would {verb} me up")
    print("As wholly as a dew")
    print(f"Upon a {flower}’s sleeve –")
    print(f"And then I started too.")

    affirmative = ['yes', 'y', 'sure', 'okay']

    user_choice = input("Do you want to continue?")    
    while user_choice.lower() in affirmative:
        print("TOIGHT, lets mAdLiB!!!")
        break
    else:
        print("Thank you for playing!")


'''
while True:
        keep_running = input('Would you like to play again? yes/no ')
        if keep_running == 'yes' or keep_running == 'no':
            break
        print('response not recognized')
 '''
#read eval print loop  'repl'
#ask a question, get an answer, use a while loop to repeat code based on input
