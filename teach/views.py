from django.contrib import messages
from django.shortcuts import render, redirect
from languages.models import Language
from django.urls import reverse
from .models import GrammarTopic
from django.contrib.auth.decorators import login_required


# Create your views here.


@login_required
def teach(request):
    languages = Language.objects.all()
    return render(request, 'teach.html', {'languages': languages})


@login_required
def teach_language(request, language):
    language_name = Language.objects.filter(name=language).first()
    return render(request, 'teach_language.html', {'language': language_name})


@login_required
def add_word(request, language):
    if request.method == 'POST':
        word = request.POST['word']
        translate = request.POST['translate']
        language = Language.objects.filter(name=language).first()
        user = request.user
        language.word_set.create(word_name=word, translate=translate, creator=user)
        # new_word = Word(word_name=word, translate=translate, language=language)
        # new_word.save()
        messages.success(request, f"New word \"{word}\" added successfully!")
        return redirect(reverse('teach_language', args=[language.name]))
    else:
        return render(request, 'teach.html')


@login_required
def add_grammar(request, language):
    lesson_name = request.POST['lesson_name']
    topic_name = request.POST['topic_name']
    topic = GrammarTopic.objects.get(topic=topic_name)
    grammar_text = request.POST['grammar_text']
    language = Language.objects.filter(name=language).first()
    user = request.user
    language.grammar_set.create(grammar_name=lesson_name, grammar_topic=topic,
                                grammar_text=grammar_text, creator=user)
    messages.success(request, f"New lesson is added successfully!")
    return redirect(reverse('teach_language', args=[language.name]))


@login_required
def add_slang(request, language):
    slang_name = request.POST['slang']
    translate_slang = request.POST['translate_slang']
    explanation = request.POST['explanation']
    user = request.user
    language = Language.objects.filter(name=language).first()
    language.slang_set.create(slang_text=slang_name, translate_text=translate_slang,
                              explanation=explanation, creator=user)
    messages.success(request, f"New slang \"{slang_name}\" is added successfully!")
    return redirect(reverse('teach_language', args=[language.name]))
