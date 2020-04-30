import json 
import requests 
import string 


#gets information from web 
url =  'http://www.gutenberg.org/cache/epub/16643/pg16643.txt'
response = requests.get(url)
print(response)
text = response.text

#created list of strings from text 
text = text.split()
print(text)


#used in lab 18
#translator is a built in variable name given by maketrans 
#clean_text takes in txt and translates it into utf-8 and translator takes in the variable translator and makes it back into text
translator = str.maketrans('', '', string.punctuation)
clean_text = txt.translate(translator) # I am a string with punctuation

clean_text =  clean_text.split()