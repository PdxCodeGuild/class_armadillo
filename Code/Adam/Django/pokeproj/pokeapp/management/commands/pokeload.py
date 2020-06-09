from django.core.management.base import BaseCommand
import requests
import json
from pokeapp.models import Pokemon, PokemonType


class Command(BaseCommand):

    def handle(self, *args, **options):

        Pokemon.objects.all.delete()
        PokemonType.objects.all.delete()

        # get json data by sending an http request
        response = requests.get('https://raw.githubusercontent.com/PdxCodeGuild/class_armadillo/master/4%20Django/labs/pokemon.json')
        data = response.text
        # print(data)
        data = json.loads(data) # turns a json string into a python dictionary
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
