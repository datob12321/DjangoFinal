from django.db import models

# Create your models here.


class Language(models.Model):
    name = models.CharField(max_length=70, unique=True)
    info = models.CharField(max_length=12000, null=False)
    img_url = models.CharField(max_length=200)
