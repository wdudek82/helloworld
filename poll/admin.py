from django.contrib import admin
from django.contrib.admin.models import LogEntry
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionModelAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline,]
    list_display = ['id', 'question_text', 'pub_date', 'updated_at', 'was_published_recently']
    list_display_links = ['question_text']

    # def get_readonly_fields(self, request, obj=None):
    #     if obj and obj.pub_date == 'cant_change_amount':
    #         return self.readonly_fields + ['pub_date']
    #     return self.readonly_fields


class ChoiceModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'choice_text', 'votes', 'question', 'question_text']
    # list_display_links = ['choice_text']
    list_editable = ['choice_text']


admin.site.register(Question, QuestionModelAdmin)
admin.site.register(Choice, ChoiceModelAdmin)
admin.site.register(LogEntry)