from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, PokemonType
import json


class Command(BaseCommand):

    def handle(self, *args, **options):
        # Pete: 'now it's the recipe, not the meal'
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()
        # write the code here
        with open('pokemon.json','r') as file:
            text = file.read()
        # the ENTIRE dictionary
        data = json.loads(text)
        # how to get these things per pokemon
        for pokemon_data in data['pokemon']:
            pokemon = Pokemon(
                name = pokemon_data['name'],
                number = pokemon_data['number'],
                height = pokemon_data['height'],
                weight = pokemon_data['weight'],
                image_front = pokemon_data['image_front'],
                image_back = pokemon_data['image_back'],
                url = pokemon_data['url'])
           
            # doing it the KWARG shortcut way
            # pokemon = Pokemon(**pokemon_data)

            pokemon.save()
         
            # list of strings, iterating
            for type_str in pokemon_data['types']:
                # unpacking 'get_or_create' not the above
                types, created = PokemonType.objects.get_or_create(name=type_str)
                # appending it
                pokemon.types.add(types)
                # when looking at SQLite - junction table has name pokemon - pokemontype (another with 's' at end)

            

          