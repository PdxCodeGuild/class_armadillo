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
                # getting out the pokemon data variable = dictionary['key']
                name   = pokemon['name']
                number    = pokemon['number']
                height     = pokemon['height']
                weight        = pokemon['weight']
                image_front = pokemon['image_front']
                image_back      = pokemon['image_back']
                types     = pokemon['types']
                # create a pokemon from our data
                # new model instance Pokemon
                pokemon = Pokemon(name=name,
                                    number=number,
                                    height=height,
                                    weight=weight,
                                    image_front=image_front,
                                    image_back=image_back,
                                    )
                # save the contact to the database
                pokemon.save()
                
                # this will go through the types and get them 
                for type in types:
                    try:
                        poke_type = PokemonType.objects.get(name=type)
                    # if the type does not exist in the database it will create one
                    except PokemonType.DoesNotExist:
                        poke_type = PokemonType.objects.create(name=type)        
                    # adding the type to the pokemon
                    pokemon.types.add(poke_type)
                # must save everytime you alter the database
                pokemon.save()