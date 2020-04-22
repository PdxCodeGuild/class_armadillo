import requests
import string

# Pulls the text from the website.
response = requests.get("http://www.gutenberg.org/cache/epub/61870/pg61870.txt")
text = response.text

# Removes liscencing stuff
text = text[text.find("***")+len("***"):text.find("End of the Project")]
text = text[text.find("***")+len("***"):]
print(text)

text = text.lower()
list_of_words = text.split()

# Loops through the list of words to get rid of any symbols.
for i in range(len(list_of_words)):
    list_of_words[i] = list_of_words[i].strip("!@#$%^&*()_+\"\':;[]\{\-=}?><,./\\")

word_dict = dict()
user_input = str()

# Used to remove blank strings from the list of words.
while True:
    try:
        # Checks to see if there is an index for a blank string, and removes it.
        if list_of_words.index("") > -1:
            list_of_words.remove("")
    # Once all the empty strings are removed, it will break because 
    # list_of_words.index("") will throw a ValueError
    except ValueError:
        break

while True:
    try:
        # Gets the user input, and checks to see if it is in the list of words. 
        # If it is in the list of words, it will break the loop.
        user_input = input("Enter a word that you wish to search from the story: ")
        if list_of_words.index(user_input) > -1:
            break
    # If the user inputs a string that is not in the list of words, it will 
    # print an appropriate message, then go back to try again.
    except ValueError:
        print("That input is not in the story.")

# For each index in the list of words, loop
for i in range(len(list_of_words)-1):
    # If the element at index 'i' is equal to the input from the user, continue.
    if list_of_words[i] == user_input:
        # Checks to see if the element at index 'i' + " " + the element at index 'i'+ 1 are in the word dictionary.
        # If they are, it will incriment their total number of occurances in the dictionary.
        # If not, it will create a new entry in the dictionary and add it once.
        if word_dict.get(list_of_words[i] + " " + list_of_words[i+1], False):
            word_dict[list_of_words[i] + " " + list_of_words[i+1]] += 1
        else:
            word_dict.setdefault(list_of_words[i] + " " + list_of_words[i+1], 1)

# word_dict is a dictionary where the key is the word and the value is the count
words = list(word_dict.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(10, len(words))):  # print the top 10 words, or all of them, whichever is smaller
    print(words[i])