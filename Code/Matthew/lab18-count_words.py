

# message = '-> hello world hello hello sunshine'
# print(message.find('hello')) # 3
# print(message.find('hello', 10)) # 15
# print(message.rfind('hello')) # 21
# exit()


import requests



# https://requests.readthedocs.io/en/master/
url = 'http://www.gutenberg.org/cache/epub/5046/pg5046.txt'
response = requests.get(url)
text = response.text
# remove junk from the start of the text
index_stars = text.find('***') # find the line that starts with "*** START OF ..."
index_stars = text.find('\n', index_stars) # find the end of that line
text = text[index_stars:] # remove everything before that index

# remove the junk at the end of the text
index_stars = text.rfind('*** END') # find the last occurance of *** END
text = text[:index_stars] # remove everything after that index
# print(text[index_stars-100:index_stars+100])




text = text.lower()

text = text.replace('--', ' ')
text = text.replace('\'', '')


# we don't care about adding extra spaces below
# split without parameters will split on combined whitespace
# print('a   a   a'.split()) # ['a', 'a', 'a']
# print('a   a   a'.split(' ')) # ['a', '', '', 'a', '', '', 'a']

for punctuation in '.!?*,()":;$-':
  text = text.replace(punctuation, ' ')

words = text.split()
print(len(words))

# returns True if the word only contains letters, otherwise returns False
def is_all_letters(word):
  for char in word:
    if char not in 'abcdefghijklmnopqrstuvwxyz':
      return False
  return True

def has_nonletter(word):
  for char in word:
    if char not in 'abcdefghijklmnopqrstuvwxyz':
      return True
  return False

# for word in words:
#   # if not is_all_letters(word):
#   if has_nonletter(word):
#     print(word, end='  ')

word_counts = {}
for word in words:
  if word in word_counts:
    word_counts[word] += 1
  else:
    word_counts[word] = 1
  
  # word_counts[word] = word_counts.get(word, 0) + 1

  # print(word_counts)



# def add(a, b):
#   return a + b
# add = lambda a, b: a + b


# look at words alphabetically to see if there are duplicates
# sorted_words = list(word_counts.keys())
# sorted_words.sort()
# print('\n'.join(sorted_words))


words = list(word_counts.items()) # .items() returns a list of tuples
words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
for i in range(min(50, len(words))):  # print the top 10 words, or all of them, whichever is smaller
  print(words[i][0], words[i][1])

