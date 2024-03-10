from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.decorators import login_required
from teach.models import Word, Slang, Grammar
from django.core.mail import send_mail

# Create your views here.


def index(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        profile_img = request.POST['profile_img']
        if password != password2:
            messages.error(request, 'Passwords do not match!')
            return redirect('register')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username is already taken!')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email is already taken!')
                return redirect('register')
            else:
                new_user = User.objects.create_user(username=username, email=email, password=password)
                new_user.save()
                login(request, new_user)
                messages.success(request, f'User {username} is  created successfully!')
                return redirect('index')
    else:
        return render(request, 'register.html')


def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'User is logged in successfully!')
            return redirect('index')
        else:
            messages.error(request, 'Username or password is incorrect!')
            return redirect('login')
    return render(request, 'login.html')


def logout_user(request):
    logout(request)
    messages.success(request, 'You are logged out successfully!')
    return redirect('login')


@login_required
def profile(request):
    words = len(request.user.word_set.all())
    slangs = len(request.user.slang_set.all())
    grammars = len(request.user.grammar_set.all())
    answers = len(request.user.answer_set.all())
    return render(request, 'profile.html', {'words_len': words, 'slangs_len':
        slangs, 'grammars_len': grammars, 'answers_len': answers})


def reset_password(request):
    if request.method == 'POST':
        old_password = request.POST['old_password']
        new_password = request.POST['new_password']
        new_password_2 = request.POST['new_password_2']
        if new_password != new_password_2:
            messages.error(request, 'Passwords do not match!')
            return redirect('profile')
        else:
            current_user = request.user
            if check_password(old_password, current_user.password):
                current_user.password = make_password(new_password)
                current_user.save()
                messages.success(request, 'Password changed successfully!')
                return redirect('login')
            else:
                messages.error(request, 'Incorrect password!')
                return redirect('profile')


def fullname(request):
    if request.method == 'POST':
        if 'submit_firstname' in request.POST:
            first_name = request.POST['firstname']
            request.user.first_name = first_name
            request.user.save()
            messages.success(request, 'Your firstname has been changed successfully!')
            return redirect('profile')
        elif 'submit_lastname' in request.POST:
            last_name = request.POST['lastname']
            request.user.last_name = last_name
            request.user.save()
            messages.success(request, 'Your lastname has been changed successfully!')
            return redirect('profile')


@login_required
def apply_content(request):
    words = Word.objects.filter(is_valid=False).all()
    grammars = Grammar.objects.filter(is_valid=False).all()
    slangs = Slang.objects.filter(is_valid=False).all()
    if request.method == 'POST':
        if 'apply_word' in request.POST:
            word = request.POST.get('word')
            word_obj = Word.objects.get(word_name=word)
            word_obj.is_valid = True
            word_obj.save()
            send_mail('About your word', f'Hello, {word_obj.creator.username}! Your word "{word}" has been applied!',
                'settings.EMAIL_HOST_USER', [word_obj.creator.email, 'davit.bitsadze.1@btu.edu.ge'],
                      fail_silently=False
            )
            return redirect('apply_content')
        elif 'delete_word' in request.POST:
            word = request.POST.get('word')
            try:
                word_obj = Word.objects.get(word_name=word)
                word_obj.delete()
                send_mail('About your added word', f'Hello, {word_obj.creator.username}! Unfortunately, '
                                             f'your word \"{word}\" has been rejected!',
                          'settings.EMAIL_HOST_USER', [word_obj.creator.email],
                          fail_silently=False
                          )
            except Exception as e:
                messages.error(request, e)
                return redirect('apply_content')
        elif 'apply_slang' in request.POST:
            slang_id = request.POST.get('slang')
            slang_obj = Slang.objects.get(id=slang_id)
            slang_obj.is_valid = True
            slang_obj.save()
            send_mail('About your added slang-expression', f'Hello, {slang_obj.creator.username}!'
                                    f'your slang-expression \"{slang_obj.slang_text}\" has been applied!',
                      'settings.EMAIL_HOST_USER', [slang_obj.creator.email],
                      fail_silently=False)
        elif 'delete_slang' in request.POST:
            slang_id = request.POST.get('slang')
            try:
                slang_obj = Slang.objects.get(id=slang_id)
                slang_obj.delete()
                send_mail('About your added slang-expression', f'Hello, {slang_obj.creator.username}!'
                                                 f'Unfortunately, your slang-expression \"{slang_obj.slang_text}\" has been rejected!',
                          'settings.EMAIL_HOST_USER', [slang_obj.creator.email],
                          fail_silently=False)
            except Exception as e:
                messages.error(request, e)
                return redirect('apply_content')
        elif 'apply_grammar' in request.POST:
            grammar_id = request.POST.get('grammar')
            grammar_obj = Grammar.objects.get(id=grammar_id)
            grammar_obj.is_valid = True
            grammar_obj.save()
            send_mail('About your added grammar lesson', f'Hello, {grammar_obj.creator.username}!'
                                                           f'your grammar lesson \"{grammar_obj.grammar_name}\" has been applied!',
                      'settings.EMAIL_HOST_USER', [grammar_obj.creator.email],
                      fail_silently=False)
        elif 'delete_grammar' in request.POST:
            grammar_id = request.POST.get('grammar')
            try:
                grammar_obj = Grammar.objects.get(id=grammar_id)
                grammar_obj.delete()
                send_mail('About your added grammar lesson', f'Hello, {grammar_obj.creator.username}!'
                                                             f'Unfortunately, your grammar lesson \"{grammar_obj.grammar_name}\" has been rejected!',
                          'settings.EMAIL_HOST_USER', [grammar_obj.creator.email],
                          fail_silently=False)
            except Exception as e:
                messages.error(request, e)
                return redirect('apply_content')


    if request.user.is_superuser:
        return render(request, 'apply_content.html', {'words': words,
                                                      'grammars': grammars, 'slangs': slangs})
    else:
        messages.error(request, 'You do not have permission to apply content!')
        return redirect('index')



