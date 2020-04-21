import requests 

response = requests.get('http://www.gutenberg.org/cache/epub/5200/pg5200.txt')
text = response.text

lines = text.split('\n')
print(lines[26:2003])

word_list = text.split()
print(word_list)
