from django.core.management.base import BaseCommand
import json

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        with open('./pokedex/management/commands/pokedex.json', 'r') as file:

            text = file.read()
            context = json.loads(text)
            pokemon = context['pokemon']

            print(pokemon)