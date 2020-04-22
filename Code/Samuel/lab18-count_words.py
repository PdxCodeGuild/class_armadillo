import requests
import string

response = requests.get("http://www.gutenberg.org/cache/epub/61870/pg61870.txt")
text = response.text

text = text[928:-19400]
print(text)

text = text.lower()
list_of_words = text.split()

for i in range(len(list_of_words)):
    list_of_words[i] = list_of_words[i].strip("!@#$%^&*()_+\"\':;[]\{\-=}?><,./\\")

word_dict = dict()
user_input = str()

while True:
    try:
        user_input = input("Enter a word that you wish to search from the story: ")
        if list_of_words.index(user_input) > -1:
            break
    except ValueError:
        print("That input is not in the story.")

test = user_input

for i in range(len(list_of_words)-1):
    if list_of_words[i] == test:
        if word_dict.get(list_of_words[i] + " " + list_of_words[i+1], False):
            word_dict[list_of_words[i] + " " + list_of_words[i+1]] += 1
        else:
            word_dict.setdefault(list_of_words[i] + " " + list_of_words[i+1], 1)

# for i in range(len(list_of_words)-1):
#     if word_dict.get(list_of_words[i] + " " + list_of_words[i+1], False):
#         word_dict[list_of_words[i] + " " + list_of_words[i+1]] += 1
#     else:
#         word_dict.setdefault(list_of_words[i] + " " + list_of_words[i+1], 1)

# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])