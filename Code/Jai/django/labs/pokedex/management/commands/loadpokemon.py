
from django.core.management.base import BaseCommand
import json
from pokedex.models import Pokemon, PokemonType

class Command(BaseCommand):


    
    def handle(self, *args, **options):
        with open('./pokedex/management/commands/pokemon.json', 'r') as file:
            text = file.read()
        data = json.loads(text)
        for pokemon in data['pokemon']:
            number = pokemon['number']
            name = pokemon['name']
            height = pokemon['height'] 
            weight = pokemon['weight']
            image_front = pokemon['image_front'] 
            image_back = pokemon['image_back'] 
            types = pokemon['types']

            new_pokemon = Pokemon(number=number,
                                name=name,
                                height=height,
                                weight=weight,
                                image_front=image_front,
                                image_back=image_back,)
            new_pokemon.save()                    
            for ptype in types:
                if ptype == types[0]:
                    p_types1 = PokemonType(name=types)
                    p_types1.save()
                elif ptype == types[1]: 
                    p_types2 = PokemonType(name=types)
                    p_types2.save()                   
            
            if len(types)== 1:
                new_pokemon.types.add(p_types1) 
            else:
                new_pokemon.types.add(p_types1, p_types2)

            # save the contact to the database
            
            
          
