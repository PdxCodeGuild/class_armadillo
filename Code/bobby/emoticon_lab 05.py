import random

# :-) ;-* 8-O 8-D >:-( :-< :-> :^) =-O =-( x-D :-} :-]

eyes = [":", ";", "8", "x", "B", ">:", "="]
eye = random.choice(eyes)

noses = ["-", "o", "^"]
nose = random.choice(noses)

mouths = [")", "(", "[", "]", "{", "}", "P", "b", "X", "O", "*", "D", ">", "<", "@", "#", "$", "/", "||", ]
mouth = random.choice(mouths)


i = 0
while i < 4:
    print(eye, nose, mouth)
    i +=1
