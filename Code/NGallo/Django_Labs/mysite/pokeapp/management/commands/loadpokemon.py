from django.core.management.base import BaseCommand
import json 
from pokeapp.models import Pokemon, PokemonType

class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('./pokeapp/management/commands/pokemon.json', 'r') as file: # open the file
            text = file.read() # read the text
            dictionary_of_pokemon = json.loads(text) # convert the text containing json into a dictionary
            pokemon_list = dictionary_of_pokemon['pokemon'] # extract the list inside the dictionary

            for pokemon in pokemon_list:
                # getting out the contact data into local variables
                name   = pokemon['name']
                number    = pokemon['number']
                height     = pokemon['height']
                weight        = pokemon['weight']
                image_front = pokemon['image_front']
                image_back      = pokemon['image_back']
                types     = pokemon['types']
                # create a contact from our data
                pokemon = Pokemon(name=name,
                                    number=number,
                                    height=height,
                                    weight=weight,
                                    image_front=image_front,
                                    image_back=image_back,
                                    )
                # save the contact to the database
                pokemon.save()
                
                for type in types:
                    try:
                        poke_type = PokemonType.objects.get(name=type)

                    except PokemonType.DoesNotExist:
                        poke_type = PokemonType.objects.create(name=type)        
                    
                    pokemon.types.add(poke_type)
                pokemon.save()