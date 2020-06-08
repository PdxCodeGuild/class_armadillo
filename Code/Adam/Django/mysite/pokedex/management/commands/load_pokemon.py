from django.core.management.base import BaseCommand
import requests
import json
from pokedex.models import Pokemon, PokemonType

class Command(BaseCommand):

    def handle(self, *args, **options):

        Pokemon.objects.delete()
        PokemonType.objects.delete()
        
        # get json data by sending an http request
        response = requests.get('https://github.com/PdxCodeGuild/class_armadillo/blob/master/4%20Django/labs/pokemon.json')
        data =  response.text
        # turn the json string into a python dictionary
        data = json.loads(data)
        pokedata = data['pokemon']
        for p in pokedata:
            number = p['number']
            name = p['name']
            height = p['height']
            weight = p['weight']
            image_front = ['image_front']
            image_back = p['image_back']
            types = p['types']

            pokemon = Pokemon(number=number,
                                name=name,
                                height=height,
                                weight=weight,
                                image_front=image_front,
                                image_back=image_back,)
            Pokemon.save()