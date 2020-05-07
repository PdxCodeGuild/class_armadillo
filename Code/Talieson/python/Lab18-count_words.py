import requests

# Lab 18 takes in a raw text version of The Brothers Grimm Fairy Tales
# and returns a list of the top 10 most common words found inside.

# Request the book from gutenberg.
response = requests.get("https://www.gutenberg.org/files/2591/2591-0.txt")

# Take in that request as text and asign it to a variable.
text = response.text
# Catch the weird UTC-8 text errors and get rid of them.
text = text.replace("â\x80\x99" or
                    "â\x80\x98" or
                    "â\x80\x9c" or
                    "â\x80\x9d", "")
# Variables defining when the story starts and ends, slice it at those points.
text_start = text.find("THE BROTHERS GRIMM FAIRY TALES")
text_end = text.find("*****")
text = text[text_start:text_end]

# Lower casing all words
text = text.lower()

# Iterating through the text getting rid of special characters.
for character in text:
    if character in (";", ".", "!", "?", "!", ",", ":", "'", "-", "â"):
        text = text.replace(character, "")

print(text)
# take the text and turn it into a list of individual words.
words = text.split()

# Empty dictionary for the word counter.
word_counts = {}

# iterate through each word in the list of words.
for word in words:
    # if the word isn't in word_counts, add it, else add 1 to count.
    if word not in word_counts:
        word_counts[word] = 1
    else:
        word_counts[word] += 1

# create a list of touples from the dictionary.
top_words = list(word_counts.items())
# sort the the list of touples based on their value.
top_words.sort(key=lambda tup: tup[1], reverse=True)
# return the top 10 touple pairs in the list of words.
for i in range(min(10, len(top_words))):
    print(top_words[i])
