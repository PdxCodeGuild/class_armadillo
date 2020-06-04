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

        data = json.loads(text)

        for pokemon_data in data['pokemon']:
            pokemon = Pokemon(
                name = pokemon_data['name'],
                number = pokemon_data['number'],
                height = pokemon_data['height'],
                weight = pokemon_data['weight'],
                image_front = pokemon_data['image_front'],
                image_back = pokemon_data['image_back'],
                url = pokemon_data['url'])

            # pokemon = Pokemon(**pokemon_data)

            pokemon.save()
            print(pokemon)

            for type_str in pokemon_data['types']:
                type, created = PokemonType.objects.get_or_create(name=type_str)

            

          