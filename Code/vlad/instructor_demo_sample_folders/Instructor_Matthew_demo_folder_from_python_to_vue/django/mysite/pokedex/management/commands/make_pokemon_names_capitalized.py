
from django.core.management.base import BaseCommand

from pokedex.models import Pokemon, PokemonType

class Command(BaseCommand):
    def handle(self, *args, **options):
        for pokemon in Pokemon.objects.all():
            pokemon.name = pokemon.name.lower()
            pokemon.save()

