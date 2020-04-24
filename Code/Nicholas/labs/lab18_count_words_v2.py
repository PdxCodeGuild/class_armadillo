#In lab 18 v2 you are searching for the most common unique word pairs in the same text as V1.
#It uses most of the same text as v1, except for the part where you iterate over the indexes 
#to search for the word pairs as commented below

import requests 

response = requests.get('http://www.gutenberg.org/cache/epub/5200/pg5200.txt') #The Metamorphosis
text = response.text

for char in text:
    if char in '[]()@$%*-.?!,\~-_:1234567890': #replace punctuation with blank space
        text=text.replace(char,' ')
text = text.lower() #makes all characters lower case

lines = text.split('\n')  #divides text into individual lines
lines[26:2003]  #defines particular lines to include(removes beginning and end fluff)

word_list = text.split()  #returns list of words
# print(word_list) #prints word list

#v2 starts here:
pair_words = {}  #creates empty dictionary for word pairs

for i in range (0, len(word_list)-1):  #iterates over word_list 
        pair = (word_list[i] + ' , ' + word_list[i+1]) #pairs word and adjacent word, separates by comma
        if pair not in pair_words: #if word pair found once, count 1 
            pair_words[pair] = 1    
        else:    #if word pair found multiple times, adds to total count
            pair_words[pair] += 1

words = list(pair_words.items())  # converts list with counts to tuples 
         
words.sort(key=lambda tup: tup[1], reverse=True)  #sorts tuples numerically, largest first
for i in range(min(10, len(words))):  #produces top 10 most frequently used words 
    print(words[i])  #prints top 10 words