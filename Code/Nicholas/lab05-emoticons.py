
import random
import time

#while loop for printing 5 more emoticons
more_emoji = True
while more_emoji: 
    #while loops here nests random facial parts to loop 5 different random emoticons
    x=0
    while x < 5:
        eyes = ["=", ":", ";","8", "!","x", "X"]#list of eyes
        random_eye = random.choice(eyes)#random choice for eyes
        noses = ["-", "^", "v", "*", "~", ">", "<", "C"]
        random_nose = random.choice(noses)
        mouths = [")", "(", "|", "[", "]", "{", "}", "O", "/", "P"]
        random_mouth = random.choice(mouths)
        print(random_eye+random_nose+random_mouth)#concatenates random part to create emoticon
        time.sleep(0.75)
        x+=1#causes while loop to reset and create new emoticon until 5 are created. ("1+2+3+4+5")    

    emoji = input("Would you like to generate 5 more random emoticons? yes/no ").lower()  #provides option to generate 5 more
    if emoji == "no":
        print("Have a nice day!") #if user selects no, prints this, then break.
        break     




    
    
