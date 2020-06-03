from django.core.management.base import BaseCommand
from pokedex.models import PokemonType, Pokemon
import json
import requests

# from .models import Pokemon
    
class Command(BaseCommand):
    def handle(self, *args, **options):

        with open('pokemon.json', 'r') as file:
            text = file.read()
            data = json.loads(text)
            for pokemans in data['pokemon']:
                number = pokemans['number']
                name = pokemans['name']
                height = pokemans['height']
                weight = pokemans['weight']
                image_front = pokemans['image_front']
                image_back = pokemans['image_back']
                types = pokemans['types']

                add_pokemon = Pokemon.objects.get_or_create(
                    number=number,
                    name=name,
                    height=height,
                    weight=weight,
                    image_front=image_front,
                    image_back=image_back,
                )
                
                for typ in types:
                    add_type, other = PokemonType.objects.get_or_create(name=types)
            # print(pokemans)