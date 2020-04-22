import requests

# Request the book from gutenberg.
response = requests.get("https://www.gutenberg.org/files/2591/2591-0.txt")

# Take in that request as text and asign it to a variable.
text = response.text
# Catch the weird UTC-8 text errors and get rid of them.
text = text.replace("\x80\x99", "").replace("\x80\x98", "").replace("\x80\x9c", "").replace("\x80\x9d", "")

# Variables defining when the story starts and ends, slice it at those points.
text_start = text.find("THE BROTHERS GRIMM FAIRY TALES")
text_end = text.find("HANS IN LUCK")
text = text[text_start:text_end]

# Lower casing all words
text = text.lower()

# Iterating through the text getting rid of special characters.
for character in text:
    if character in (";", ".", "!", "?", "!", ",", ":", "'", "-", "â"):
        text = text.replace(character, "")

# take the text and turn it into a list of individual words.
words = text.split()

# Empty dictionary for the word counter.
word_pairs = {}

# iterate through each word in the list of words.
for word in range(len(words)-1):
    if word_pairs.get(words[word] + " " + words[word+1], False):
        word_pairs.update({words[word] + " " + words[word+1]: 1})
    else:
        word_pairs[word] += 1
# create a list of touples from the dictionary.
top_word_pairs = list(word_pairs.items())
# sort the the list of touples based on their value.
top_word_pairs.sort(key=lambda tup: tup[1], reverse=True)

# return the top 10 touple pairs in the list of words.
for i in range(min(10, len(top_word_pairs))):
    print(top_word_pairs[i])
