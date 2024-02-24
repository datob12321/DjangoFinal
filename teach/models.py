from django.contrib.auth.models import User
from django.db import models
from languages.models import Language
from learn.models import Question
from datetime import datetime

# Create your models here.


class Word(models.Model):
    word_name = models.CharField(max_length=100, null=False, unique=True)
    translate = models.CharField(max_length=100, null=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class GrammarTopic(models.Model):
    topic = models.TextField(max_length=1000, null=False)


class Grammar(models.Model):
    grammar_name = models.CharField(max_length=1000, null=False)
    grammar_topic = models.ForeignKey(GrammarTopic, on_delete=models.CASCADE)
    grammar_text = models.TextField(max_length=120000, null=False, unique=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False)

class Slang(models.Model):
    slang_text = models.TextField(max_length=200, null=False, unique=True)
    translate_text = models.CharField(max_length=200, null=False)
    explanation = models.CharField(max_length=1000, null=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Answer(models.Model):
    answer_text = models.CharField(max_length=100000, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    address = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(default=datetime.now, blank=True)

