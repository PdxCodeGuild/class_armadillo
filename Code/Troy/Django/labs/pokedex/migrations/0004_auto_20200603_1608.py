# Generated by Django 3.0.6 on 2020-06-03 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokedex', '0003_auto_20200603_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='image_front',
            field=models.ImageField(upload_to='admin/'),
        ),
    ]
