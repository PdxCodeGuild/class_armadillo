import random

# :-) ;-* 8-O 8-D >:-( :-< :-> :^) =-O =-( x-D :-} :-]

eyes_list = [":", ";", "8", "x", "B", ">:", "="]
noses_list = ["-", "o", "^"]
mouths_list = [")", "(", "[", "]", "{", "}", "P", "b", "X", "O", "*", "D", ">", "<", "@", "#", "$", "/", "||", ]



i = 0
while i < 5:
    eyes =  random.choice (eyes_list)
    noses = random.choice (noses_list)
    mouths  = random.choice (mouths_list)
    
    print(eyes + noses + mouths)
    i +=1
