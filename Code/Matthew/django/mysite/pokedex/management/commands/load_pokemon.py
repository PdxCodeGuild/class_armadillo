
from django.core.management.base import BaseCommand

# from .models import Pokemon

class Command(BaseCommand):
    def handle(self, *args, **options):
        with open('./pokedex/management/commands/pokemon.json', 'r') as file:
            text = file.read()
            print(text)
