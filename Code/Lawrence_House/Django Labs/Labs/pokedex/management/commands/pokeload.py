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

                add_pokemon = Pokemon(
                    number=number,
                    name=name,
                    height=height,
                    weight=weight,
                    image_front=image_front,
                    image_back=image_back,
                )
                add_pokemon.objects.get_or_create()

                for types in pokemon['types']:
                    add_type = PokemonType.objects.get_or_create(name=pokemon_type,)[0]
                    if add_type not in add_pokemon.types.all():
                        add_type.types.add(add_type)
                        add_type.pokemon_set.add(add_pokemon)
            # print(pokemans)