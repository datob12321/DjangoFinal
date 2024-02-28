from django.urls import path
from . import views


urlpatterns = [
    path('', views.learn, name='learn'),
    path('<str:language>/', views.learn_language, name='learn_language'),
    path('<str:language>/words/', views.learn_words, name='learn_words'),
    path('<str:language>/grammar_topics/', views.grammar_topics, name='grammar_topics'),
    path('<str:language>/grammar_topics/<str:topic>/', views.grammar_lessons, name='grammar_lessons'),
    path('<str:language>/slangs', views.slangs_lessons, name='slangs'),
    path('<str:language>/make_question', views.make_question, name='make_question')
]


