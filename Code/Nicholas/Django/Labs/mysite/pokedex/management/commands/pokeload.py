from django.core.management.base import BaseCommand
import json
from pokedex.models import PokemonType, Pokemon
class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('./pokedex/management/commands/pokemon.json', 'r') as file:
            text = file.read()
        data = json.loads(text)    
        print(data)
        for pokemon_data in data['pokemon']:
            number = pokemon_data['number']
            name = pokemon_data['name']
            height = pokemon_data['height']
            weight = pokemon_data['weight']
            image_front = pokemon_data['image_front']
            image_back = pokemon_data['image_back']
            types = pokemon_data['types']

            load_pokemon = Pokemon(number=number,
                                   name=name,
                                   height=height,
                                   weight=weight,
                                   image_front=image_front,
                                   image_back=image_back,
                                   )
            load_pokemon.save()  
        for types in pokemon['types']:
            load_type = PokemonType.objects.get_or_create(name=poketype,)
            if load_type not in load_pokemon.types.all():                     

                    
                 

                       