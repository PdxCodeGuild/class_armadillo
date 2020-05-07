# 2) get a clean list of words ['the', 'the', 'a', 'that', 'hello', 'that', ..]

def word_list(text):
  words_list = []
  for letter in remove_punc:
    text = text.replace(letter, ' ')
  print(text)
  exit()
  words = text.lower().split()
  for word in words:
    words_list.append(words)
  for i in range(len(words)):
    words[i] = words