from django.contrib import admin
from .models import Hello, Example, Question, Choice


class QuestionModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question_text', 'pub_date']


class ChoiceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'question', 'choice_text', 'votes']


class HelloModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'message']

    class Meta:
        model = Hello


class ExampleModelAdmin(admin.ModelAdmin):
    list_display = ['pk', 'tag', 'created_at']

    class Meta:
        model = Example


admin.site.register(Question, QuestionModelAdmin)
admin.site.register(Choice, ChoiceModelAdmin)
admin.site.register(Hello, HelloModelAdmin)
admin.site.register(Example, ExampleModelAdmin)
