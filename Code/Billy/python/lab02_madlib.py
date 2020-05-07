print('\nWELCOME TO MADLIBS...where your words complete the story! \n') # welcome msg

# user input variables to fill into madlib blanks
holiday = input('What is your favorite holiday? ') 
noun = input('In which room/building are you currently? ')
thing = input('Look up! What\'s the first object you see? ') # escape so that ' is printed
body_part1 = input('What is your favorite body part? ')
verb1 = input('What do you do like to do when happy (verb)? ')
verb2 = input('What do you do whenever you\'re sad (verb)? ')
body_part2 = input('What is your LEAST favorite body part? ')

see_story = input('Would you like to see your story? (yes/no) ') # prompts user to continue to story or leaves program

if see_story == 'yes': # will print below madlib f string that fills in the above variables in the appropriate {}
    print('-'*80) # visual border
    print(f'''\nIt's close to {holiday} and something evil's lurkin' in the {noun}. 
Under the {thing}, you see a sight that almost stops your {body_part1}.
You try to {verb1} but terror takes the sound before you make it.
You start to {verb2} as horror looks you right between the {body_part2}.
You're paralyzed!\n''')
    print('-'*80)
elif see_story != 'yes': # prints good bye message and leaves program if see_story input is anything but yes
     print('GOOD BYE...have a nice day!')




'''
Lab 2: Mad Libs

Write a simple program that prompts the user for several inputs then
 prints a [Mad Lib](https://en.wikipedia.org/wiki/Mad_Libs) as the result.

## Instructions

1. Search the interwebs for an example Mad Lib
2. Ask the user for each word you'll put in your Mad Lib
3. Use `string concatenation` to put each word into the Mad Lib

## Example:

```
>>> Give me an antonym for 'data': nonmaterial
>>> Tell me an adjective: Bearded
>>> Give me a sciency buzzword: half-stack
>>> A type of animal (plural): parrots
>>> Some Sciency thing: warp drive
>>> Another sciency thing: Trilithium crystals
>>> Sciency adjective: biochemical
...
>>> Nonmaterial Scientist Job Description:
>>> Seeking a bearded engineer, able to work on half-stack projects with a team of parrots.
>>> Key responsibilities:
>>> - Extract patterns from non-material
>>> - Optimize warp drive
>>> - Transform trilithium crystals into biochemical material.
```


## Version 2 (optional)

* Make a functional solution that utilizes lists. For example, ask the user for 3 adjectives, separated by commas, then use the .split() function to store each adjective and later use it in your story.
* Add randomness! Use the random module, rather than selecting which adjective goes where in the story.


## Version 3 (optional)
* Make it a repeatable game. Once you're done prompting the user for words, prompt them for whether they'd like to hear the story. Use a while loop to keep asking if they'd like to hear the story again until the answer is 'no'. You could then ask them if they'd like to make another story, and so on.


## Key Concepts

- Variables
- String formatting
- Handling user input
'''    