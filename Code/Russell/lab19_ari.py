import requests
import re
import math
import string
book = requests.get('https://www.gutenberg.org/cache/epub/375/pg375.txt')

text = book.text

index_stars = text.find('***') 
index_stars = text.find('\n', index_stars) 
text = text[index_stars:]


index_stars = text.rfind('*** END') 
text = text[:index_stars]

# sentences = re.split('. |? ',str(text))
# print(sentences)



text_list = text.split()  
for i in range(len(text_list)):
    text_list[i] = text_list[i].strip('1234567890@#$%^&*()_-;][]:}{\'\",/;:\\|<>')

word_length = []
for element in text_list:
    word_length.append(len(element))

word_length_average = 4.71 * (sum(word_length) / len(text_list))

# text_string = ''.join(text_list)

# print(re.split('. |? ', text_string))






