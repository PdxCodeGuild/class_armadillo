# 1-2

# https://github.com/PdxCodeGuild/class_armadillo/blob/master/1%20Python/labs/lab02-madlib.md

# Lab 2: Mad Libs
# Write a simple program that prompts the user for several inputs then prints a Mad Lib as the result.

# Instructions
# 1. Search the interwebs for an example Mad Lib
# 2. Ask the user for each word you'll put in your Mad Lib
# 3. Use string concatenation to put each word into the Mad Lib

# Suzy had a little ________ (noun), its ____________(texture)
#  was white as ______(noun).
import random

texture = ["wool", "hair" , "mane"]
texture = random.choice(texture)

noun = input("What is the first noun you wish to name? ")

noun2 = input("What is the second noun you wish to name? ")

print(f"Suzy had a little {noun}, its {texture} was white as {noun2}" ) 