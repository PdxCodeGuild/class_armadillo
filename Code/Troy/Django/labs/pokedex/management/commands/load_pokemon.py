from django.core.management.base import BaseCommand
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        # data = [{}]
    # opens the file.
        with open('./pokedex/management/commands/pokebase.json', 'r') as file:
        # reads the text
            text = file.read()
            context = json.loads(text)
            pokemon = context['pokemon']

            print(pokemon)
            

    
       