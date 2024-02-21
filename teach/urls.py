from django.urls import path
from . import views

urlpatterns = [
    path('', views.teach, name='teach'),
    path('<str:language>/', views.teach_language, name='teach_language'),
    path('<str:language>/add-word', views.add_word, name='add_word')
]
