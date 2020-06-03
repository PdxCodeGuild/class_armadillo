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
            poke_mon = Pokemon.objects.get_or_create(
                name=pokemon['name'].title(),
                number=int(pokemon['number']),
                height=int(pokemon['height']),
                weight=int(pokemon['weight']),
                image_front=pokemon['image_front'],
                image_back=pokemon['image_back'],
                url=pokemon['url'],                
            )[0]

            # create db objects for types and set up relations to pokemon
            for typ in pokemon['types']:
                poke_type, created = PokemonType.objects.get_or_create(name=typ)

                if poke_type not in poke_mon.types.all():
                    poke_mon.types.add(poke_type)
                    poke_type.pokemon.add(poke_mon)

                
                
