from django.contrib import admin
from .models import GrammarTopic, Answer,Grammar, Word, Slang

admin.site.register(Word)
admin.site.register(GrammarTopic)
admin.site.register(Grammar)
admin.site.register(Slang)
admin.site.register(Answer)

# Register your models here.
