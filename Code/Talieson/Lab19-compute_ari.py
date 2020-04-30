from re import findall
from math import ceil


# define the path and open text file
text_path = "C:/Users/talie/class_armadillo/code/talieson/data/Ion.txt"
with open(text_path, "r") as file:
    text = file.read()


# find and replace odd characters with blank string
def text_clean(text):
    for character in text:
        if character in (";", ".", "!", "?", "!", ",",
                         ":", "'", "-", "â", "(", ")"):
            text = text.replace(character, "")
    return text


# take our text in and return a list of word
def word_count(text):
    # we need to call clean text function
    text = text_clean(text)
    word_list = []
    words = text.lower().split()
    # iterate over words, add them all to the list
    for word in words:
        word_list.append(word)
    return len(word_list)


# count the characters in the text
def character_count(text):
    # call our text cleaning function
    text = text_clean(text)
    characters = 0
    # if what is left is a letter, iterate our character count
    for character in text:
        if character.isalpha():
            characters += 1
    return characters


# Use regex to catch all instances of sentences and return that number
def sentence_count(text):
    sentence_pattern = (r'([^\.\?\!]*)[\.\?\!]')
    sentences = len(findall(sentence_pattern, text))
    return sentences


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

# define the beginning and end of the text, and split it to those points
text_start = "PERSONS OF THE DIALOGUE: Socrates, Ion."
text_end = "End of the Project Gutenberg EBook of Ion, by Plato"
text = text[text.find(text_start):text.find(text_end)]

# call our functions, and define them in variables
num_of_words = word_count(text)
sentences = sentence_count(text)
characters = character_count(text)

# use variables to dermine the ARI
ari = ceil(((characters/num_of_words) * 4.71) +
           ((num_of_words/sentences) * .5) - 21.43)

# print ARI information
print(f'''
    --------------------------------------------------------

    The ARI for Ion.txt is {ari}
    This corresponds to a {ari_scale[ari]["grade_level"]} difficulty
    that is suitable for an average person {ari_scale[ari]["ages"]} years old.

    --------------------------------------------------------''')
