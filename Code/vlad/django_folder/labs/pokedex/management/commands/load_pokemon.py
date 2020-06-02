from django.core.management.base import BaseCommand

# from .models import Pokemon
import json


class Command(BaseCommand):
    def handle(self, *args, **options):
        # we need to add the relative path here
        with open('./pokedex/management/commands/pokemon.json', 'r') as file:
            text = file.read()
            context = json.loads(text)
            pokemon = context['pokemon']
            print(pokemon)
