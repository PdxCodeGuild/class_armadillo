'''Write a simple program that prompts the user for several inputs then prints a Mad Lib as the 
result.

Instructions
Search the interwebs for an example Mad Lib
Ask the user for each word you'll put in your Mad Lib
Use string concatenation to put each word into the Mad Lib'''

# mad lib that was utilized for the lab.

'''A vacation is when you take a trip to some __________________ place 
 your __________________ family. Usually you go to some place 
that is near a/an __________________ or up on a/an __________________. 
A good vacation place is one where you can ride __________________ 
or play __________________ or go hunting for __________________ . I like 
to spend my time ________________________ or ________________________.
When parents go on a vacation, they spend their time eating 
three __________________ a day, and fathers play golf, and mothers 
sit around ________________________. Last summer, my little brother 
fell in a/an __________________ and got poison __________________ all 
over his________________________. My family is going to go to (the) 
 
__________________, and I will practice ________________________. Parents 
need vacations more than kids because parents are always very 
 
__________________ and because they have to work__________________ 
hours every day all year making enough __________________ to pay 
for the vacation.'''

# allows a delay to be placed withing the code.
import time

# assigns the user answer when prompted. 
adjective = input ('enter adjective: ')
adjective2 = input ('enter adjective2: ')
noun = input ('enter noun: ')
noun2 = input ('enter noun2: ')
nouns = input ('enter nouns: ')
game = input ('enter game: ')
nouns2 = input ('enter nouns2: ')
verb = input ('enter verb:  ')
verb2 = input ('enter verb2:  ')
nouns3 = input ('enter nouns3: ')
verb3 = input ('enter verb3:  ')
noun4 = input ('enter noun4: ')
plant = input ('enter plant: ')
part_of_a_boy = input ('enter part_of_a_boy: ')
a_place = input ('enter a_place: ')
verb4 = input ('enter verb4: ')
adjective3 = input ('enter adjective3: ')
number = input ('enter number: ')
nouns4 = input ('enter nouns4: ')

# provides a delay from the last entered answer to the mad lib for dramatic effect.
time.sleep(1)

# the mad lib in a 'f' string to allow the input to be placed where needed.
print (f''''A vacation is when you take a trip to some {adjective} place 
your {adjective2} family. Usually you go to some place 
that is near a/an {noun} or up on a/an {noun2}. 
A good vacation place is one where you can ride {nouns} 
or play {game} or go hunting for {nouns2} . I like 
to spend my time {verb} or {verb2}.
When parents go on a vacation, they spend their time eating 
three {nouns3} a day, and fathers play golf, and mothers 
sit around {verb3} . Last summer, my little brother 
fell in a/an {noun4} and got poison {plant} all 
over his {part_of_a_boy}. My family is going to go to  
{a_place}, and I will practice {verb4} . Parents 
need vacations more than kids because parents are always very {adjective3} and because they have to work {number} 
hours every day, all year long making enough {nouns4} to pay for the vacation.''')
