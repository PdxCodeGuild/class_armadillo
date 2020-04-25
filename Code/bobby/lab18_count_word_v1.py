import requests # request package
import string
# 1.)Requesting the URL
response = requests.get("http://www.gutenberg.org/cache/epub/5200/pg5200.txt")

# Define the text that you want, in this case it is Metamorphosis by Franz Kafka
text = response.text
# print(text)

# 2.) To define a clean list of words within the text
clean_list = text.split("r")
print(clean_list[26 : 2003])

for char in text:
    if char in "1234567890-=!@#$%^&*()_+,./\|":
        text = text.replace(char, " ")
text = text.lower()

lines = text.split("\n")

word_list = text.split()

#3.) To build a word count dict for the value of a word and count.
count = {}
for word in word_list:
    if word not in count:
        count[word] = 1   
    else:
        count[word] += 1
words = list(count.items())# .items() returns a list of tuples
print(words)

words.sort(key=lambda tup: tup[1], reverse = True)# Sorts largest to smallest, based on count. 
for i in range(min(10, len(words))):# print the top 10 words, or all of them, whichever is smaller
    print(words[i])