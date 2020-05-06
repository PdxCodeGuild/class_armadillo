# Lab 05 Random Emoticon Generator
# Import Random to generate random Emoticons
import random

# :-) ;-* 8-O 8-D >:-( :-< :-> :^) =-O =-( x-D :-} :-]

# My list of diffrent Eyes, Noses and Mouths for the program to pull from when generating the random emoticons
eyes_list = [":", ";", "8", "x", "B", ">:", "="]
noses_list = ["-", "o", "^"]
mouths_list = [")", "(", "[", "]", "{", "}", "P", "b", "X", "O", "*", "D", ">", "<", "@", "#", "$", "/", "||", ]


# The While loop is to generate 5 diffrent randomly built emoticons
i = 0
while i < 5:
    eyes =  random.choice (eyes_list)
    noses = random.choice (noses_list)
    mouths  = random.choice (mouths_list)
# This is to show the user the 5 diffrent emoticons that the program built    
    print(eyes + noses + mouths)
    i +=1
