from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, PokemonType  
import json

class Command(BaseCommand):

    def handle(self, *args, **options):

        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()
        # opens the file.
        with open('./pokedex/management/commands/pokebase.json', 'r') as file:
            # reads the text in the file.
            text = file.read()
            data = json.loads(text)
            for pokemon in data['pokemon']:
                number = pokemon['number']
                name   = pokemon['name']
                height = pokemon['height']
                weight = pokemon['weight']
                image_front = pokemon['image_front']
                image_back = pokemon['image_back']
                types  = pokemon['types']

            pokemon_data = Pokemon(number=number,
                    name=name,
                    height=height,
                    weight=weight,
                    image_front=image_front,
                    image_back= image_back,
                    types=types)
            pokemon_data.save()

# MAKE IT LOOK LIKE THE VIEWS PAGE FROM CONTACTS!!!

            print(pokemon)
            

    
       