import json
from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, PokemonType
# from .models import Pokemon

#erases current tables from database if need to redo load
Pokemon.objects.all().delete()
PokemonType.objects.all().delete()

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('./pokedex/management/commands/pokemon.json', 'r') as file: # open file via relative path
            data = json.loads(file.read()) # read the file and convert json to dictionary

        # looping over the contact data inside that dictionary
        for pokemon_data in data['pokemon']:
            number = pokemon_data['number']
            name = pokemon_data['name']
            height = pokemon_data['height']
            weight = pokemon_data['weight']
            image_front = pokemon_data['image_front']
            image_back = pokemon_data['image_back']
            url = pokemon_data['url']
        
            pokemon = Pokemon(number=number,
                                name=name,
                                height=height,
                                weight=weight,
                                image_front=image_front, 
                                image_back=image_back,
                                url=url)
            pokemon.save()

        for typ_data in pokemon_data['types']:
            pok_typ, created = PokemonType.objects.get_or_create(name=typ_data)
            pokemon.types.add(pok_typ)
            # if pokemon_type not in pokemon.types.all():
            #     pokemon.types.add(pokemon_type)
            #     pokemon_type.pokemons.add(pokemon) #related name set in models
            # pokemon_type.save()

        # pokemon_type.save()
        # print(data)
        # print(pokemon)
        # print(type)
        # print(pokemon.types.all())
        # print(pokemon_type.pokemons.all())
        