
from django.core.management.base import BaseCommand

import requests
import json

from pokedex.models import Pokemon, PokemonType

class Command(BaseCommand):
    def handle(self, *args, **options):

        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()

        # response = requests.get('https://raw.githubusercontent.com/PdxCodeGuild/class_armadillo/master/4%20Django/labs/pokemon.json')
        # print(response.text)

        with open('./pokedex/management/commands/pokemon.json', 'r') as file:
            text = file.read()
        data = json.loads(text)
        for pokemon_data in data['pokemon']:
            # pokemon = Pokemon(**pokemon_data)
            # pokemon.types=...

            pokemon = Pokemon(number=pokemon_data['number'],
                                name=pokemon_data['name'],
                                height=pokemon_data['height'],
                                weight=pokemon_data['weight'],
                                image_front=pokemon_data['image_front'],
                                image_back=pokemon_data['image_back'],
                                url=pokemon_data['url'])
            pokemon.save()

            for type_str in pokemon_data['types']:
                type, created = PokemonType.objects.get_or_create(name=type_str)
                # type = PokemonType(name=type_str)
                # type.save()

                pokemon.types.add(type)
            

        
# def kwargs(**data):
#     print(data)
# kwargs(a=1,b=2,c=3)
# kwargs(**{'a':1, 'b':2, 'c':3})