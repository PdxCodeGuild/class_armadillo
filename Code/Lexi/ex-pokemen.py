import requests

# 1) get the text from the file, via "with open..." or using requests

response = requests.get('https://raw.githubusercontent.com/LazoCoder/Pokemon-Terminal/master/pokemonterminal/Data/pokemon.txt')
text = response.text
print(text)


#capitalize the pokemon names
big = text.upper(text)
print(big)

# split strings
