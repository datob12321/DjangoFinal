from django.contrib import admin
from .models import GrammarTopic, Answer,Grammar, Word, Slang, Status, Test

admin.site.register(Word)
admin.site.register(GrammarTopic)
admin.site.register(Grammar)
admin.site.register(Slang)
admin.site.register(Answer)
admin.site.register(Status)
admin.site.register(Test)

# Register your models here.
