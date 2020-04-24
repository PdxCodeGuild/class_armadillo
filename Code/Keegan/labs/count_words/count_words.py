import requests
from string import punctuation

response = requests.get("http://www.gutenberg.org/cache/epub/5200/pg5200.txt")

text = response.text


for punc in punctuation:
    text = text.replace(punc, '')


text = text.replace('\r', '').split('\n')[20:len(text)-100]

start = 0
end = 0

# find the beginning and the end of the text
# based on number of whitespace lines on either side
# definitely not the most dynamic method, though
# it will work if there are at least 4 whitespace
# lines before and after the main text
for i in range(2, len(text)):
    if text[i] != '':
        next_5 = text[i:i+5]
        if start == 0:
            if len([i for i in next_5 if i == '']) == 0:
                start = i
        else:
            if len([i for i in next_5 if i == '']) == 4:
                end = i


text = text[start:end+1]

# remove all Roman numeral chapter numbers
for i in range(len(text)-1, 0, -1):
    if len(text[i]) < 3:
        text.pop(i)

text = [item.split(' ') for item in text]

words = []

# add each word in each line in text to the list of words if it's not a blank string
[[words.append(text[i][j].lower()) for j in range(len(text[i])) if text[i][j] != ''] for i in range(len(text))]

print(words)