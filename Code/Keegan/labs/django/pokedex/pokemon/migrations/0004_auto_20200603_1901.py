# Generated by Django 3.0.6 on 2020-06-03 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokemon', '0003_auto_20200603_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='types',
            field=models.ManyToManyField(related_name='pokemon', to='pokemon.PokemonType'),
        ),
    ]
