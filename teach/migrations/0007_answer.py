# Generated by Django 5.0.2 on 2024-02-24 09:25

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('languages', '0001_initial'),
        ('learn', '0003_initial'),
        ('teach', '0006_delete_answer'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=100000)),
                ('date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learn.question')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='languages.language')),
            ],
        ),
    ]
