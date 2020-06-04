from django.core.management.base import BaseCommand
import json
from .  import Pokemon, PokemonType

class Command(BaseCommand):

    def handle(self, *args, **options):
        # write the code here
        Pokemon.objects.all().delete()
        PokemonType.objects.all().delete()
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

            new_pokemon = Pokemon(
                number= number,
                name = name,
                height = height,
                weight = weight,
                image_front = image_front,
                image_back = image_back,
                types = types,
                )

            new_pokemon.save()
            for pokemon_types in types:
                pokemon_types_new,created = PokemonType.object.get_or_create(name=pokemon_types)
                new_pokemon.types.add(pokemon_types_new)

