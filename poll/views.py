from django.shortcuts import render, reverse, get_object_or_404
from django.views.generic import View
from .models import Question


class Mixins:
    @classmethod
    def get_abs_url(cls, url, key, value):
        return reverse(url, kwargs={key: value})


class Index(View, Mixins):
    context = {
        'questions': Question.objects.order_by('-pub_date')[:5]
    }

    def get(self, request):
        return render(request, 'poll/index.html', self.context)


class Detail(View, Mixins):
    def get(self, request, id=None):
        question = get_object_or_404(Question, id=id)
        context = {
            'question': question,
        }
        return render(request, 'poll/detail.html', context)
