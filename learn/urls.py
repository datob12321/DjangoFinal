from django.urls import path
from . import views


urlpatterns = [
    path('', views.learn, name='learn'),
    path('<str:language>/', views.learn_language, name='learn_language')
]


