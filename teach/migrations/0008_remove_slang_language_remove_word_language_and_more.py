# Generated by Django 5.0.2 on 2024-02-24 11:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teach', '0007_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slang',
            name='language',
        ),
        migrations.RemoveField(
            model_name='word',
            name='language',
        ),
        migrations.DeleteModel(
            name='Grammar',
        ),
        migrations.DeleteModel(
            name='Slang',
        ),
        migrations.DeleteModel(
            name='Word',
        ),
    ]
