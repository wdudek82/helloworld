from django.shortcuts import render, reverse
from django.views.generic import View
from .models import Question


class Mixins:
    @classmethod
    def get_abs_url(cls, url, key, value):
        return reverse(url, kwargs={key: value})


class Index(View, Mixins):
    context = {
        'questions': Question.objects.all()
    }

    def get(self, request):
        return render(request, 'poll/index.html', self.context)
