# Generated by Django 3.0.6 on 2020-06-02 13:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='age',
        ),
    ]
