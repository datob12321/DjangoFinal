from django.db import models
from django.contrib.auth.models import User
from languages.models import Language
from datetime import datetime

# Create your models here.


class Question(models.Model):
    question_text = models.CharField(max_length=100000, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False)
    pub_date = models.DateTimeField(default=datetime.now, blank=True)



