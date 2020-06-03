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

                pokemon_data, created = Pokemon.objects.get_or_create(number=number,
                        name=name,
                        height=height,
                        weight=weight,
                        image_front=image_front,
                        image_back= image_back)
                # print(pokemon_data)
                # types = PokemonType.objects.get_or_create(name=types)
                for typ in types:                                 
                    powers, created = PokemonType.objects.get_or_create(name=typ)
                    if powers not in pokemon_data.types.all():
                        pokemon_data.types.add(powers)
                        powers.pokemon.add(pokemon_data)
                # pokemon_data.save()



                    




            
            

    
       