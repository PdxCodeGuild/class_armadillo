from django.core.management.base import BaseCommand


class Command(BaseCommand):

    def handle(self, *args, **options):
        with open('pokemon.json', 'r') as file:
            data = json.loads(file.read())
        return data
        pass
             