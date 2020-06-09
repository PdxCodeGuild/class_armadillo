from django.core.management.base import BaseCommand

import requests
import json
from .  import Pokemon, PokemonType

class Command(BaseCommand):

    def handle(self, *args, **options):
        # write the code here
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()
        with open('./pokedex/management/commands/pokemon.json', 'r') as file:
            text = file.read()
        data = json.loads(text)
        for pokemon in data['pokemon']:

            pokemon = Pokemon(
                number = pokemon['number'],
                name = pokemon['name'],
                height = pokemon['height'],
                weight = pokemon['weight'],
                image_front = pokemon['image_front'],
                image_back = pokemon['image_back'],
                url = pokemon['url'],
                types = pokemon['types']
                )
            pokemon.save()
            
            new_pokemon = Pokemon(
                number = pokemon['number'],
                name = pokemon['name'],
                height = pokemon['height'],
                weight = pokemon['weight'],
                image_front = pokemon['image_front'],
                image_back = pokemon['image_back'],
                types = pokemon['types']
                )
            new_pokemon.save()
            
        for type_str in pokemon['types']:
            type, created = PokemonType.objects.get_or_create(name=type_str)
        
            pokemon.types.add(type)


