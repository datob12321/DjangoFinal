from django.shortcuts import render
from languages.models import Language

# Create your views here.


def learn(request):
    languages = Language.objects.all()
    return render(request, 'learn.html', {'languages': languages})


def learn_language(request, language):
    language_name = Language.objects.filter(name=language).first()
    return render(request, 'learn_language.html', {'language': language_name})
