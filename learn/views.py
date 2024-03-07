from django.core import serializers
from django.shortcuts import render, redirect
from languages.models import Language
from teach.models import GrammarTopic, Slang
from django.urls import reverse
from django.contrib import messages
from .models import Question
from teach.models import Answer
from django.core import paginator

# Create your views here.


def learn(request):
    languages = Language.objects.all()
    return render(request, 'learn.html', {'languages': languages})


def learn_language(request, language):
    language_name = Language.objects.filter(name=language).first()
    questions = Question.objects.filter(language=language_name)
    questions_json = serializers.serialize('json', questions)
    answers = Answer.objects.all()
    answers_json = serializers.serialize('json', answers)
    return render(request, 'learn_language.html',
                  {'language': language_name,
                          'json_questions': questions_json, 'questions': questions,
                   'json_answers': answers_json})


def learn_words(request, language):

    language_obj = Language.objects.filter(name=language).first()
    all_words = language_obj.word_set.filter(is_valid=True).order_by('word_name'.lower())
    # order_by('word_name'.lower())
    dict_words = [{'word': word.word_name, 'translate': word.translate} for word in all_words]

    #json_words = serializers.serialize('json', all_words)
    page = request.GET.get('page')
    page_obj = paginator.Paginator(all_words, 10)
    page_obj = page_obj.get_page(page)
    return render(request, 'words.html', {'page_words': page_obj,
                                          'json_words': dict_words, 'language_obj': language_obj})


def grammar_topics(request, language):
    language_obj = Language.objects.filter(name=language).first()
    topics = GrammarTopic.objects.all()
    return render(request, 'grammar_list.html', {'topics': topics,
                                                 'language': language_obj})


def grammar_lessons(request, language, topic):
    topic_obj = GrammarTopic.objects.filter(topic=topic).first()
    language_obj = Language.objects.filter(name=language).first()
    lessons = language_obj.grammar_set.filter(grammar_topic=topic_obj, is_valid=True)
    lessons_json = serializers.serialize('json', lessons)
    return render(request, 'grammar_lessons.html', {"lessons": lessons,
                                                    "topic": topic_obj, "lessons_json": lessons_json})


def slangs_lessons(request, language):
    language_obj = Language.objects.filter(name=language).first()
    slangs = language_obj.slang_set.filter(is_valid=True).all()
    return render(request, 'slangs.html', {'slangs': slangs})


def make_question(request, language):
    question = request.POST.get('question')
    language_obj = Language.objects.filter(name=language).first()
    user = request.user
    language_obj.question_set.create(question_text=question, user=user)
    messages.success(request, 'Question has been successfully added!')
    return redirect(reverse('learn_language', args=[language_obj.name]))


