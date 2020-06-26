from django.core.management.base import BaseCommand
from pokedex.models import Pokemon, PokemonType
import json


class Command(BaseCommand):


    
    def handle(self, *args, **options):
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()
        with open('./pokedex/management/commands/pokemon.json', 'r') as file:
            text = file.read()
        data = json.loads(text)
        print(data)
        pokemon = data['pokemon']
        print(pokemon)
        
        for pokemon_data in data['pokemon']:
            pokemon = Pokemon(number = pokemon_data['number'],
                                name = pokemon_data['name'],
                                height = pokemon_data['height'], 
                                weight = pokemon_data['weight'],
                                image_front = pokemon_data['image_front'], 
                                image_back = pokemon_data['image_back'])

            pokemon.save()

            for type_str in pokemon_data['types']:
                type, created = PokemonType.objects.get_or_create(name=type_str)
                pokemon.types.add(type)

            pokemon.save()