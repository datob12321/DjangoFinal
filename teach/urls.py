from django.urls import path
from . import views

urlpatterns = [
    path('', views.teach, name='teach'),
    path('<str:language>/', views.teach_language, name='teach_language'),
    path('<str:language>/add-word', views.add_word, name='add_word'),
    path('<str:language>/add-grammar', views.add_grammar, name='add_grammar'),
    path('<str:language>/add-slang', views.add_slang, name='add_slang')
]
