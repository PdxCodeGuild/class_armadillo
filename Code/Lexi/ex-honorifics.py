# based off of lab 19

import re

def count_sentences(text):
  text = text.lower()
  # this would not work for something like, "he is the best."
  honorifics = ['st.', 'mr.', 'dr.', 'ms.']
  for honorific in honorifics:
    text = text.replace(honorific, honorific.replace(',', ''))
  # return text.count(',') + text.count('?') + text.count('!')
  # counter = 0
  # for char in text:
  #   if char == '.' or char == '?' or char == '!':
  #     counter += 1
  # return counter
  results = re.split(r'[.?!')

  def count_words(text):
    # words = text.split()
    # return len(words)
    results = re.findall(r"[\w;]+", text)
    return len(results)

    results = re.split(r'\s', text)
    print(results)

  def count_characters(text):
    # return len(text)
    results = re.findall(r'[a-zA-Z]', text)
    return len(results)

  text = '''Snippet from the 19th century:
A quote, which I recently discovered gives some more hints where to look for specific information about aquatic life. In the  “Cyclopaedia; Or, Universal Dictionary of Arts, Sciences and Literature” (1819), Abraham Rees provided a list of classic and early modern Ichthyologist:

“ICHTHYOLOGISTS, authors who have written concerning fishes. The authors who have left us treaties on this subject are very numerous; and are ranged by Artedi into there several proper classes, with great care and candour.

The systematical ichthyologists are Aristotle, Isidore, Albertus Magnus, Gaza, the interpreter of Aristotle, Marschall, Wootton, Bellonius, Rondeletius, Salvian, Gesner, Aldrovand, Johnston, Charlton,Willughby, Ray, Artedi, and Linnaeus.'''



print(f'{sentences=}')
print(f'{words=}')

ari = 4.71*(characters/words) + 0.5*(words/sentences) - 21.43
print(ari)
ari = round(ari) # round to the nearest whole number
ari = int(ari)
ari = math.floor(ari)
ari = math.ceil(ari) #     

print(f'ARI is {ari} which is {ari_scale[ari][ages]} which is {ari_scale[ari]}')