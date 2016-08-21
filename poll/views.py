from django.shortcuts import render, reverse, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.views.generic import View, RedirectView
from .models import Question, Choice


class Mixins:
    @classmethod
    def get_abs_url(cls, url, key, value):
        return reverse(url, kwargs={key: value})


class Index(View):
    context = {
        'questions': Question.objects.order_by('-pub_date')[:5]
    }

    def get(self, request):
        return render(request, 'poll/index.html', self.context)


class Detail(View):
    def get(self, request, id=None):
        question = get_object_or_404(Question, id=id)
        context = {
            'question': question,
        }
        return render(request, 'poll/detail.html', context)


class Results(View):
    def get(self, request, id=None):
        context = {
            'question': get_object_or_404(Question, id=id)
        }
        return render(request, 'poll/result.html', context)


# TODO: Rewrite it as Class-Based View
def vote(request, id=None):
    question = get_object_or_404(Question, id=id)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'poll/index.html', {
            'questions': Questions.objects.order_by('-pub_date')[:5],
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return redirect(reverse('poll:result', args=(question.id,)))

