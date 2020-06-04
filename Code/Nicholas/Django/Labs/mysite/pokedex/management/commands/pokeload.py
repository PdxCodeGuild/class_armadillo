from django.core.management.base import BaseCommand
import json
from pokedex.models import Pokemon, PokemonType


class Command(BaseCommand):

    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()
        with open('./pokedex/management/commands/pokemon.json', 'r') as file:
            text = file.read()
            data = json.loads(text)    
        
        for pokemon in data['pokemon']: 
            number = pokemon['number']
            name = pokemon['name']
            height = pokemon['height']
            weight = pokemon ['weight']
            image_front = pokemon['image_front']
            image_back = pokemon['image_back']
            types = pokemon['types']
            
            
            load_pokemon, created = Pokemon.objects.get_or_create(number = int(pokemon['number']),
                        name = name,
                        height = height,
                        weight = weight,
                        image_front = image_front,
                        image_back = image_back)
                        
            for pokemon_type in pokemon['types']:
                load_pokemon_type, created = PokemonType.objects.get_or_create(name=pokemon_type)

                if load_pokemon_type not in load_pokemon.types.all():
                    load_pokemon.types.add(load_pokemon_type)
                    load_pokemon_type.pokemon.add(load_pokemon)

                load_pokemon.save()  
          


        
                
                    
                 

                       