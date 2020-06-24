

from django.core.management.base import BaseCommand
import requests
import json
from pokeapp.models import Pokemon, PokemonType

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()

        # get json data by sending an http request
        response = requests.get('https://raw.githubusercontent.com/PdxCodeGuild/class_armadillo/master/4%20Django/labs/pokemon.json')
        data = response.text
        # turn the json string into a python dictionary
        data = json.loads(data)
        # print(data['pokemon'][59]) # poliwag
        pokedata = data['pokemon']
        for p in pokedata:
            number = p['number']
            name = p['name']
            height = p['height']
            weight = p['weight']
            image_front = p['image_front']
            image_back = p['image_back']
            types = p['types']

            pokemon = Pokemon(number=number,
                                name=name,
                                height=height,
                                weight=weight,
                                image_front=image_front,
                                image_back=image_back)
            pokemon.save()
            for type_str in types:
                # get the PokemonType with the given name if it exists
                # if it doesn't, create it
                type, created = PokemonType.objects.get_or_create(name=type_str)
                pokemon.types.add(type)

            
        