
from django.core.management.base import BaseCommand

# from .models import Pokemon

class Command(BaseCommand):
    def handle(self, *args, **options):
        print('you just ran a custom management command!')
