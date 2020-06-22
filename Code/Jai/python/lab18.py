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


count = {} 


    if char not in count: 
        count[char] = 1
    elif char in count: 
        count[char] += 1

words = list(count.items())
words.sort(key=lambda tup: tup[1], reverse=True)  

for i in range(min(10, len(words)
        print(words[i])



