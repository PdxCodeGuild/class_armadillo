import json
from django.core.management.base import BaseCommand
from pokemon.models import Pokemon, PokemonType

class Command(BaseCommand):

    def handle(self, *args, **options):
        # open pokemon json file
        with open('pokemon.json', 'r') as pokemon_file:
            all_pokemon = json.load(pokemon_file)['pokemon']

        # create DB entries for pokemon
        for pokemon in all_pokemon:
            p_mon = Pokemon.objects.get_or_create(
                name=pokemon['name'],
                number=int(pokemon['number']),
                height=int(pokemon['height']),
                weight=int(pokemon['weight']),
                image_front=pokemon['image_front'],
                image_back=pokemon['image_back'],
                url=pokemon['url'],                
            )[0]

            # create db objects for types and set up relations to pokemon
            for t in pokemon['types']:
                p_type, created = PokemonType.objects.get_or_create(name=t)

                if p_type not in p_mon.types.all():
                    p_mon.types.add(p_type)
                    p_type.pokemon.add(p_mon)

                
                
