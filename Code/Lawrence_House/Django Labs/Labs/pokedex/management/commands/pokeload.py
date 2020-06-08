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
                number = int(pokemans['number'])
                name = pokemans['name']
                height = int(pokemans['height'])
                weight = int(pokemans['weight'])
                image_front = pokemans['image_front']
                image_back = pokemans['image_back']
                types = pokemans['types']

                add_pokemon = Pokemon(
                    number=number,
                    name=name,
                    height=height,
                    weight=weight,
                    image_front=image_front,
                    image_back=image_back,
                )
                add_pokemon.save()
                for typ in types:
                    add_type, other = PokemonType.objects.get_or_create(name=typ)
                    add_pokemon.types.add(add_type)
                    
            # print(pokemans)