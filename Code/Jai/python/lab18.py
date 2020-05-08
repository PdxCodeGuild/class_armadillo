import requests
import string



url = 'http://www.gutenberg.org/cache/epub/16643/pg16643.txt'
response = requests.get(url)
#print(response)
txt = response.text.lower()

#print(txt)

list_of_words = txt.split()

#print(list_of_words)


    

#translator is a built in variable name given by maketrans 
#clean_text takes in txt and translates it into utf-8 and translator takes in the variable translator and makes it back into text
translator = str.maketrans('', '', string.punctuation)
clean_text = txt.translate(translator) # I am a string with punctuation



clean_text = clean_text.split()

#word_dict = clean_text
#print(clean_text[:100])

count = {} #this is a dictionary containing the words as keys and their values 

#for loop iterates over the text and decides that if the word isnt in the dictionary that it should be added to the dictionary
for char in clean_text:
    if char not in count: 
        count[char] = 1
    elif char in count: 
        count[char] += 1

words = list(count.items()) #returns a list of tuples

words.sort(key=lambda tup: tup[1], reverse=True) #sort the largest to the smallest 

for i in range(min(10, len(words))): #prints the top 10 of words from largst to smallest
        print(words[i])



