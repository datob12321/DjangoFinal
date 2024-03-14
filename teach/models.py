from django.contrib.auth.models import User
from django.db import models
from languages.models import Language
from learn.models import Question
from datetime import datetime
from django.core.exceptions import ValidationError

# Create your models here.


class Word(models.Model):
    word_name = models.CharField(max_length=100, null=False, unique=True)
    translate = models.CharField(max_length=100, null=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False)
    is_valid = models.BooleanField(default=False, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class GrammarTopic(models.Model):
    topic = models.TextField(max_length=1000, null=False)


def validate_lesson_name(value):
    if len(value) < 15:
        raise ValidationError("Name must be at least 15 characters long!")


def validate_grammar_text(value):
    if len(value) < 120:
        raise ValidationError("Text must be at least 120 characters long!")


class Grammar(models.Model):
    grammar_name = models.CharField(max_length=1000, null=False, unique=True, validators=[validate_lesson_name])
    grammar_topic = models.ForeignKey(GrammarTopic, on_delete=models.CASCADE)
    grammar_text = models.TextField(max_length=120000, null=False, unique=True, validators=[validate_grammar_text])
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False)
    is_valid = models.BooleanField(default=False, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


class Slang(models.Model):
    slang_text = models.TextField(max_length=200, null=False, unique=True)
    translate_text = models.CharField(max_length=200, null=False)
    explanation = models.CharField(max_length=1000, null=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False)
    is_valid = models.BooleanField(default=False, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, null=False)


def validate_answer(value):
    if len(value) < 20:
        ValidationError('Answer is too short!')


class Answer(models.Model):
    answer_text = models.TextField(max_length=100000, null=False, validators=[validate_answer])
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    address = models.ForeignKey(Question, on_delete=models.CASCADE, null=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=False)
    date = models.DateTimeField(default=datetime.now, blank=True)


class Status(models.Model):
    teacher_status = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)


class Test(models.Model):
    question = models.CharField(max_length=1000)
    a = models.CharField(max_length=500)
    b = models.CharField(max_length=500)
    c = models.CharField(max_length=500)
    d = models.CharField(max_length=500)
    correct_answer = models.CharField(max_length=1, choices=[('a', 'a'), ('b', 'b'), ('c', 'c'), ('d', 'd')], null=False)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

