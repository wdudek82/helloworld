from django.contrib import admin
from .models import Question, Choice


class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'pub_date', 'was_published_recently']


class ChoiceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'choice_text', 'votes']


admin.site.register(Question, QuestionModelAdmin)
admin.site.register(Choice, ChoiceModelAdmin)
