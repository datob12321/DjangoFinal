from django.contrib import messages
from django.shortcuts import render, redirect
from languages.models import Language
from teach.forms import WordForm
from teach.models import Word


# Create your views here.


def teach(request):
    languages = Language.objects.all()
    return render(request, 'teach.html', {'languages': languages})


def teach_language(request, language):
    language_name = Language.objects.filter(name=language).first()
    return render(request, 'teach_language.html', {'language': language_name})


def add_word(request, language):

    if request.method == 'POST':
        word = request.POST['word']
        translate = request.POST['translate']
        language = Language.objects.filter(name='Spanish').first()
        language.word_set.create(word_name=word, translate=translate)
        # new_word = Word(word_name=word, translate=translate, language=language)
        # new_word.save()
        messages.success(request, f"New word \"{word}\" added successfully!")
        return redirect('teach')
    else:
        return render(request, 'teach.html')
