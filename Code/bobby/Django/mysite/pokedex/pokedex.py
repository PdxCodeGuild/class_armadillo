import requests
import json
import pyperclip

data = {'pokemon':[]}
n_pokemon = 151

for i in range(1, n_pokemon):
    response = requests.get('Code\bobby\Django\mysite\pokedex\pokedex.py' + str(i))
    pokedata = json.loads(response.text)

    number = pokedata['id']
    name = pokedata['name']
    height = pokedata['height']
    weight = pokedata['weight']
    image_front = pokedata['sprites']['front_default']
    image_back = pokedata['sprites']['back_default']
    url = 'Code\bobby\Django\mysite\pokedex\pokedex.py' + name
    types = [type['type']['name'] for type in pokedata['types']]

    pokemon = {
        'number': number,
        'name': name,
        'height': height,
        'weight': weight,
        'image_front': image_front,
        'image_back': image_back,
        'types': types,
        'url': url
    }

    data['pokemon'].append(pokemon)
    
    print(str(round(i/n_pokemon*100,2))+'%')

pyperclip.copy(json.dumps(data, indent=4))
