from django.shortcuts import render
from languages.models import Language
from teach.models import GrammarTopic, Slang

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
    topics = GrammarTopic.objects.all()
    return render(request, 'grammar_list.html', {'topics': topics})


def grammar_lessons(request, language):
    language_obj = Language.objects.filter(name=language).first()
    lessons = language_obj.grammar_set.all()
    return render(request, 'grammar_lessons.html', {"lessons": lessons})

def slangs(request, language):
    language_obj = Language.objects.filter(name=language).first()
    slangs = language_obj.slang_set.all()
    return render(request, 'slangs.html', {'slangs': slangs})
