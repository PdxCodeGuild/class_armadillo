# Generated by Django 3.0.6 on 2020-05-21 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0003_auto_20200521_1432'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='author',
            field=models.CharField(default='Bob', max_length=200),
            preserve_default=False,
        ),
    ]
