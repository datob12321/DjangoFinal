from django.forms import ModelForm
from languages.models import Language
from .models import Answer


# class WordForm(forms.Form):
#     word = forms.CharField(max_length=100, required=True)
#     translate = forms.CharField(max_length=100, required=True)


# class GrammarForm(ModelForm):
#     class Meta:
#         model = Grammar
#         fields = ['grammar_name', 'grammar_topic', 'grammar_text']
#
#     def clean(self):
#         super(GrammarForm, self).clean()
#         grammar_name = self.cleaned_data['grammar_name']
#         grammar_text = self.cleaned_data['grammar_text']


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['answer_text']

    def clean(self):
        super(AnswerForm, self).clean()
        answer_text = self.cleaned_data['answer_text']

