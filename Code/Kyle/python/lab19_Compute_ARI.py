#   Lab 19 Version
#   Kyle Harasimowicz

# Imports/Admin variables
import requests
import string
import re 
import math
not_a_letter = "`~-!@#$%^&*()_+=?:;,.\"”[]}{â€1234567890™"
not_a_letter2 = "`~-@#$%^&*()_+=:;,\"”[]}{â€1234567890™"



# ARI Scale Dictionary
ari_scale = {
     1: {'ages':   '5-6', 'grade_level': 'Kindergarten'},
     2: {'ages':   '6-7', 'grade_level':    '1st Grade'},
     3: {'ages':   '7-8', 'grade_level':    '2nd Grade'},
     4: {'ages':   '8-9', 'grade_level':    '3rd Grade'},
     5: {'ages':  '9-10', 'grade_level':    '4th Grade'},
     6: {'ages': '10-11', 'grade_level':    '5th Grade'},
     7: {'ages': '11-12', 'grade_level':    '6th Grade'},
     8: {'ages': '12-13', 'grade_level':    '7th Grade'},
     9: {'ages': '13-14', 'grade_level':    '8th Grade'},
    10: {'ages': '14-15', 'grade_level':    '9th Grade'},
    11: {'ages': '15-16', 'grade_level':   '10th Grade'},
    12: {'ages': '16-17', 'grade_level':   '11th Grade'},
    13: {'ages': '17-18', 'grade_level':   '12th Grade'},
    14: {'ages': '18-22', 'grade_level':      'College'}
}


#OPENING LINE
print("\nWelcome to Lab 19. Let's check to see how many characters, words, and sentences are in Jack London's Classic, 'Call of the Wild.' \n")
print("Please be patient - depending on the size of the text, this download might take a few seconds. \n")

# import the text to be evaluated from internet
response  = requests.get('https://www.gutenberg.org/files/215/215-0.txt')
text = response.text.lower()

# open text file from path
# text_path = "C:/Users/kdhar/class_armadillo/code/kyle/call_of_the_wild.txt"
# with open(text_path, "r") as file:
#     text = file.read()

# Clean text to remove all admin information, move to lower-case
text = text[text.find("*** start of this project gutenberg ebook"):text.find("end of this project gutenberg ebook")]

# Clean text to remove UTC Codes, extranious punctuation.
def mr_clean_1(text):
    text = text.replace('â€™', '\'').replace('\x80\x99', '\'').replace('\x80\x94', '\'').replace('\x80\x9d', '\'').replace('\x80\x9c', '\'').replace('-', ' ')
    text = text.replace('â€', '\"').replace('â€œ', '\"')
    text = text.replace('start of this project gutenberg ebook', '')
    text = text.replace('start of the project gutenberg ebook', '')
    text = text.replace('end of the project gutenberg ebook', '')
    for letter in not_a_letter:
        text = text.replace(letter, '')
    text = text.replace('  ', ' ').replace('   ', ' ')
    return text

# Clean text to remove UTC Codes, extraneous punctuation. Leaves periods to determine # of sentences
def clean_for_sentence_count(text):
    text = text.replace('â€™', '\'').replace('\x80\x99', '\'').replace('\x80\x94', '\'').replace('\x80\x9d', '\'').replace('\x80\x9c', '\'').replace('-', ' ')
    text = text.replace('â€', '\"').replace('â€œ', '\"').replace('!', '.').replace('?', '.')
    for letter in not_a_letter2:
        text = text.replace(letter, '')
    text = text.replace('  ', ' ').replace('   ', ' ')
    return text

# function to take text, turn it into a block of characters, and count
def character_count(text):
    mr_clean_1(text)
    # generate a clean block of characters
    textblock = text
    textblock = textblock.replace(' ', '').replace("'", "").replace('"', "")
    # to remove all 'white space' and line breaks
    textblock = textblock.split()
    # and concatenate the entire text as a single string
    textblock = ''.join(textblock)
    char_count = 0
    for i in textblock:
        char_count += 1
    return char_count

# Unfinished second function using "isalpha()" to generate a character count
def character_count_2(text):
    # generate a clean block of text
    textblock = text
    textblock = textblock.replace(' ', '')
    char_count = 0
    for i in textblock:
        while textblock.isalpha():
            char_count += 1
    return char_count

# Split text into a list of words  and generate a word count 
def word_count(text):
    mr_clean_1(text)
    text = text.split()
    word_count = 0
    for i in text:
        word_count += 1
    return word_count

# Function to clean the text of extraneous punctuation
# remove all spaces between words
# remove all line breaks and white space by putting all words into a list
# concatenating that list into a single string
# and then splitting all the sentences by each period to create a list of sentences
# and finally, counting all sentence elements in the new list to give a sentence count.
def how_many_sentences(text):
    text = text.replace('â€™', '\'').replace('\x80\x99', '\'').replace('\x80\x94', '\'').replace('\x80\x9d', '\'').replace('\x80\x9c', '\'')#.replace('-', ' ')
    text = text.replace('â€', '\"').replace('â€œ', '\"').replace('!', '.').replace('?', '.')
    text = text.replace('start of this project gutenberg ebook', '')
    text = text.replace('start of th project gutenberg ebook', '')
    text = text.replace('end of the project gutenberg ebook', '')
    #print(f"Should be lines of prose with punctuation: {text[:100]}")
    for letter in not_a_letter2:
        text = text.replace(letter, '')
    # create a text block (line breaks still exist)
    text = text.replace('  ', '').replace('   ', '').replace(' ', '')
    textblock = text
    #print(f"Should be lines of prose without punctuation or spacing: {textblock[:100]}")
    # to remove all 'white space' and line breaks
    textblock = textblock.split()
    #print(f"Should be a list of words: {textblock[:100]}")
    # and concatenate the entire text as a single string
    textblock = ''.join(textblock)
    #print(f"Should be a line of characters: {textblock[:100]}")
    list_of_sentences = re.split("\.", textblock)
    #print(F"Should be a list of full sentences: {list_of_sentences[:100]}")
    number_of_sentences = 0
    for i in list_of_sentences:
        number_of_sentences += 1
    
    return number_of_sentences

#run the functions to generate each answer
character_count(text)
word_count(text)
how_many_sentences(text)

# format the answers to add commas in the thousands place
format_characters = "{:,}".format(character_count(text))
format_words = "{:,}".format(word_count(text))
format_sentences = "{:,}".format(how_many_sentences(text))

# ARI ScoreVariables
a = character_count(text) / word_count(text)
b = word_count(text) / how_many_sentences(text)

#print statements to display the results for the user
print(f"The Call of the Wild has: \n")
print(f"Characters: {format_characters}")
print(f"Word Count: {format_words}")
print(f"Sentence Count: {format_sentences}\n")

#FOLLOW-UP LINE
print(f"\nThe automated readability index (ARI) is a formula for computing the U.S. grade level for a given block of text. The general formula to compute the ARI is as follows: \n")


# Calculate the answers
ari_score = (4.71 * a) + (0.5 * b) - 21.43
print(f"The ARI Score is: {round(ari_score, 2)}, rounded up to {math.ceil(ari_score)}.\n")
ari_score = math.ceil(ari_score)

# Print the results
print(f"--------------------------------------------------------")
print(f"The ARI for Call of the Wild is {ari_score} ")
print(f"This corresponds to a {ari_scale[ari_score]['grade_level']} level of difficulty")
print(f"that is suitable for an average person {ari_scale[ari_score]['ages']} years old.")
print(f"--------------------------------------------------------\n")




