from django.core import serializers
from django.shortcuts import render, redirect
from languages.models import Language
from teach.models import GrammarTopic, Slang
from django.urls import reverse
from django.contrib import messages

# Create your views here.


def learn(request):
    languages = Language.objects.all()
    return render(request, 'learn.html', {'languages': languages})


def learn_language(request, language):
    language_name = Language.objects.filter(name=language).first()
    return render(request, 'learn_language.html', {'language': language_name})


def learn_words(request, language):

    language_obj = Language.objects.filter(name=language).first()
    all_words = language_obj.word_set.order_by('word_name'.lower())
    # all_words = Word.objects.filter(language.name == language).order_by('word_name')
    return render(request, 'words.html', {'all_words': all_words})


def grammar_topics(request, language):
    language_obj = Language.objects.filter(name=language).first()
    topics = GrammarTopic.objects.all()
    return render(request, 'grammar_list.html', {'topics': topics,
                                                 'language': language_obj})


def grammar_lessons(request, language, topic):
    topic_obj = GrammarTopic.objects.filter(topic=topic).first()
    language_obj = Language.objects.filter(name=language).first()
    lessons = language_obj.grammar_set.filter(grammar_topic=topic_obj)
    lessons_json = serializers.serialize('json', lessons)
    return render(request, 'grammar_lessons.html', {"lessons": lessons,
                                                    "topic": topic_obj, "lessons_json": lessons_json})


def slangs_lessons(request, language):
    language_obj = Language.objects.filter(name=language).first()
    slangs = language_obj.slang_set.all()
    return render(request, 'slangs.html', {'slangs': slangs})


def make_question(request, language):
    question = request.POST.get('question')
    language_obj = Language.objects.filter(name=language).first()
    user = request.user
    language_obj.question_set.create(question_text=question, user=user)
    messages.success(request, 'Question has been successfully added!')
    return redirect(reverse('learn_language', args=[language_obj.name]))


