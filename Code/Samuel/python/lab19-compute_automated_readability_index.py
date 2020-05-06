# PDX Code Guild Fullstack Course
# Lab 19 Compute Automated Readability Index
# Samuel Purdy
# 4/28/2020
import requests
import re
import string

# ARI scaling
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
# Creates the pattern that's used to break a string into a list of
# sentences while also removing the '*' character.
pattern = re.compile(r"[^.!?*]+")

# Pulls the text from the website.
address = "http://www.gutenberg.org/cache/epub/61870/pg61870.txt"

def make_sentences(web_address):
    text = requests.get(web_address).text
    # text = response.text


    # Removes liscencing stuff
    text = text[text.find("***")+len("***"):text.find("End of the Project")]
    text = text[text.find("***")+len("***"):]

    # Removes whitespace operators
    text = text.replace("\n", " ")
    text = text.replace("\t", " ")
    text = text.replace("\r", "") # Windows has \r on some new-lines

    # Splits the text into a list of strings based on where the periods,
    # exclamation marks, and question marks are.
    sentences = pattern.findall(text)

    # Strips sentences of noise characters that serve no purpose
    for i in range(len(sentences)):
        sentences[i] = sentences[i].strip(" ,\"'")

    # Loops until all blank strings are removed.
    while True:
        try:
            # Checks to see if there is an index for a blank string,
            # and removes it.
            if sentences.index("") > -1:
                sentences.remove("")
        # Once all the empty strings are removed, it will break because 
        # list_of_words.index("") will throw a ValueError
        except ValueError:
            break
    return sentences

# Gets the ARI score based on the text.
# list_of_sentences = block of text to be scored with ARI
def get_score(list_of_sentences):
    
    # Initialized variables
    list_of_words_in_sentence = list()
    number_of_words = 0
    avg_words = int()
    list_of_characters_in_words = list()
    number_of_characters = 0
    avg_characters = int()

    # Counts the number of words in a single sentence, then counts 
    # the number of characters in each word in each sentence
    for i in range(len(list_of_sentences)):
        list_of_words = list_of_sentences[i].split()
        list_of_words_in_sentence.append(len(list_of_words))
        for j in range(len(list_of_words)):
            list_of_characters_in_words.append(len(list_of_words[j]))

    # Records the number of characters
    for i in range(len(list_of_characters_in_words)):
        number_of_characters += list_of_characters_in_words[i]

    # Records the number of words
    for i in range(len(list_of_words_in_sentence)):
        number_of_words += list_of_words_in_sentence[i]

    # Average calculations are done seperately for clarity.
    avg_characters = number_of_characters/len(list_of_characters_in_words)
    avg_words = number_of_words/len(list_of_words_in_sentence)

    # Returns the rounded number based on the values given.
    return round(4.71 * avg_characters + 0.5 * avg_words - 21.43)

# Used to print the score and the grade level at which the text is usually for.
# score = score based on ARI
def print_score(score):
    print("----------------------------------------------------------------------------")
    print(f"The ARI for {address} is {score}")
    print(f"This corresponds to a " + ari_scale[score]["grade_level"] + " level of difficulty")
    print(f"that is suitable for an average person " + ari_scale[score]['ages'] + " years old")
    print("----------------------------------------------------------------------------")

# For testing Purposes
if __name__ == "__main__":

    sentences = make_sentences(address)
    score = get_score(sentences)
    print_score(score)
    
    address1 = "http://www.gutenberg.org/cache/epub/61950/pg61950.txt"
    address2 = "https://www.gutenberg.org/files/61960/61960-0.txt"
    address3 = "https://www.gutenberg.org/files/61955/61955-0.txt"
    
    print_score(get_score(make_sentences(address1)))
    print_score(get_score(make_sentences(address2)))
    print_score(get_score(make_sentences(address3)))
