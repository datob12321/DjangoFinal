# Generated by Django 5.0.2 on 2024-02-23 19:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
        ('teach', '0002_delete_slang'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slang_text', models.TextField(max_length=200, unique=True)),
                ('translate_text', models.CharField(max_length=100)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.language')),
            ],
        ),
    ]