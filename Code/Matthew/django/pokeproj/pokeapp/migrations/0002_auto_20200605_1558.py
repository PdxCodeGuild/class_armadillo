# Generated by Django 3.0.6 on 2020-06-05 22:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='pokemontype',
            options={'ordering': ['name']},
        ),
    ]
