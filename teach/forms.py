from django import forms
from languages.models import Language


class WordForm(forms.Form):
    word = forms.CharField(max_length=100, required=True)
    translate = forms.CharField(max_length=100, required=True)

