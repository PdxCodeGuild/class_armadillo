import requests
import string



url = 'http://www.gutenberg.org/cache/epub/16643/pg16643.txt'
response = requests.get(url)
#print(response)
txt = response.text.lower()

#print(txt)

list_of_words = txt.split()




translator = str.maketrans('', '', string.punctuation)
clean_text = txt.translate(translator) 



clean_text = clean_text.split()


count = {} #this is a dictionary containing the words as keys and their values 

#for loop iterates over the text and decides that if the word isnt in the dictionary that it should be added to the dictionary
for char in clean_text:
    if char not in count: 
        count[char] = 1
    elif char in count: 
        count[char] += 1

words = list(count.items()) #returns a list of tuples
print(words)
words.sort(key=lambda tup: tup[1], reverse=True) #sort the largest to the smallest 

for i in range(min(10, len(words))): #prints the top 10 of words from largst to smallest
        print(words[i])



