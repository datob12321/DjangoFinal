from django.contrib import messages
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.http import HttpResponse
from django.shortcuts import render, redirect
from languages.models import Language
from django.urls import reverse
from .forms import AnswerForm
from learn.models import Question
from .models import GrammarTopic, Grammar
from django.contrib.auth.decorators import login_required
from django.core import paginator


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
        word = request.POST['word'].lower()
        translate = request.POST['translate']
        language = Language.objects.filter(name=language).first()
        user = request.user
        if user.is_superuser:
            language.word_set.create(word_name=word, translate=translate, creator=user, is_valid=True)
            messages.success(request, f"New word \"{word}\" added successfully!")
        else:
            language.word_set.create(word_name=word, translate=translate, creator=user)
            messages.success(request, f"Your word \"{word}\" will be reviewed!")
        return redirect(reverse('teach_language', args=[language.name]))
    else:
        return render(request, 'teach.html')


@login_required
def add_grammar(request, language):
        grammar_name = request.POST['lesson_name']
        topic_name = request.POST['topic_name']
        grammar_text = request.POST['grammar_text']
        user = request.user
        language = Language.objects.filter(name=language).first()
        topic = GrammarTopic.objects.filter(topic=topic_name).first()

        new_grammar = Grammar.objects.create(grammar_name=grammar_name, grammar_topic=topic,
                                             grammar_text=grammar_text, language=language, creator=user)
        try:
            new_grammar.full_clean()
        except ValidationError as err:
            messages.error(request, f'Grammar lesson is not valid! - {err.messages}')
            return redirect(reverse('teach_language', args=[language.name]))
        else:
            new_grammar.save()
            messages.success(request, 'New grammar lesson is added successfully!')
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


@login_required
def questions_view(request, language):
    answer_form = AnswerForm()
    language = Language.objects.filter(name=language).first()
    questions = Question.objects.filter(language=language)
    paginate = paginator.Paginator(questions, 4)
    page = request.GET.get('page')
    page_obj = paginate.get_page(page)
    return render(request, 'questions.html', {'questions': page_obj,
                                              "answer_form": answer_form})


@login_required
def make_answer(request, language):
    language = Language.objects.filter(name=language).first()
    answer_form = AnswerForm(request.POST)
    print(answer_form.data)
    try:
        if answer_form.is_valid():
            answer = answer_form.save(commit=False)
            answer.language = language
            answer.author = request.user
            address_id = request.GET.get('address')
            address_user = Question.objects.get(id=address_id)
            answer.address = address_user
            answer.save()
            messages.success(request, 'Answer has been saved!')
            return redirect(reverse('questions_view', args=[language.name]))
        else:
            print(answer_form.message)
    except Exception as e:
        return HttpResponse(e)

