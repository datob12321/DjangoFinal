# Generated by Django 5.0.2 on 2024-03-05 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0020_grammar_is_valid'),
    ]

    operations = [
        migrations.AddField(
            model_name='slang',
            name='is_valid',
            field=models.BooleanField(default=False),
        ),
    ]
