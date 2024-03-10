from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('reset_password/', views.reset_password, name='reset_password'),
    path('update_fullname', views.fullname, name='fullname'),
    path('apply_content', views.apply_content, name='apply_content'),
    path('password_reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('set_password/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_confirm_view'),
    path('password_reset_complete/', PasswordResetCompleteView.as_view(), name='password_reset_complete')
]
