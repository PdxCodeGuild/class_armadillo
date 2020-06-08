from django.core.management.base import BaseCommand
import json
from pokedex.models import Pokemon, PokemonType


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('./db.json', 'r') as file:
            data = json.loads(file.read())
        for pokemon in data['pokemon']:
            instance_of_pokemon = Pokemon.objects.get_or_create(number=int(pokemon['number']),
                                  name=pokemon['name'],
                                  height=int(pokemon['height']),
                                  weight=int(pokemon['weight']),
                                  image_front=pokemon['image_front'],
                                  image_back=pokemon['image_back'],
            )[0]  #get_or_create returns a tuple and the infomration is stored in first index

            for pokemon_type in pokemon['types']:
                instance_of_pokemon_type = PokemonType.objects.get_or_create(name=pokemon_type,)[0]
                if instance_of_pokemon_type not in instance_of_pokemon.types.all():
                    instance_of_pokemon.types.add(instance_of_pokemon_type)
                    instance_of_pokemon_type.pokemon_set.add(instance_of_pokemon)  # _set is nessiary to create the handshake.. still noe 100% why
