from django.core.management.base import BaseCommand
import json


class Command(BaseCommand):

    def load_pokemon(self, *args, **options):
        # open the file containing the json
        with open('./pokedex/management/commands/pokemon.json', 'r') as file:
            # reading the text in the file
            text = file.read()
            data = json.loads(text)
            pokemon = data('pokemon')
        pass
