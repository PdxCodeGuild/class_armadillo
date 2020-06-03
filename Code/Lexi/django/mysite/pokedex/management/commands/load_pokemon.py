from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, PokemonType
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokedex.objects.all().delete
        # write the code here
        with open('./pokedex/management/commands/pokemon.json','r') as file:
            text = file.read()

        data = json.loads(text)

        for pokemon in data['pokemon']:
            name = pokemon['name']
            number = pokemon['number']
            height = pokemon['height']
            weight = pokemon['weight']
            image_front = pokemon['image_front']
            image_back = pokemon['image_back']
            types = pokemon['types']

            pokemon = Pokemon(name=name,
                                number=number,
                                height=height,
                                weight=weight,
                                image_front=image_front,
                                image_back=image_back)
            pokemon.save()

            print(pokemon)