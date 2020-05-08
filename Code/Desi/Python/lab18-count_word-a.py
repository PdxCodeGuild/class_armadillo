import requests


# 1) get the text from the file, via "with open..." or using requests

response = requests.get('http://www.gutenberg.org/cache/epub/23540/pg23540.txt')
text = response.text
# print(text)

# returns a list of strings after breaking the given string by the specified separator.
lines =  text.split('\r')
# limit text file to lines 200 - 800
paragraph = lines[200:800]
# print text selection
print(paragraph)

# ===============================================================================


# Make everything lowercase,  strip punctuation, split into a 
# list of words
# AttributeError: 'list' object has no attribute 'lower'
string2 = paragraph.lower(str(paragraph))
print(string2)
x = string2.replace("o", "")
print(x)
 # ==========================================================

# strip punctuation
for character in text:
    if character in (";", ":", ",", "!", "?", "'"):
      text = text.replace(character, "")

print(text)

# ==========================================================


# Split into a list of words

x = txt.split()
print(x)
txt = ""
x = txt.split()
print(x)


#=================================================================================

# 3A. Your dictionary will have words as `keys` and counts as `values`.

#iterate each word in list of words
word_counts = {}
 for keys in x:
     if keys not in word_counts:
         word_counts[keys] = 1
