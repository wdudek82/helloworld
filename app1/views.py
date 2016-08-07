from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.views.decorators.http import require_safe, require_http_methods
from django.views.generic import View, RedirectView, DetailView
from .models import Example
from .forms import ExampleForm


# @require_safe
# def example(request, slug=None):
#     example_obj = get_object_or_404(Example, slug=slug)
#     context = {
#         'example_obj': example_obj,
#         'request': request,
#         'examples': Example.objects.all()
#     }
#     return render(
#         request,
#         'app1/example.html',
#         context
#     )
#
# @require_http_methods(['GET', 'HEAD', 'POST'])
# def example_create(request):
#     if request.method == 'POST':
#         form = ExampleForm(request.POST)
#         example_obj = form.save()
#         return redirect(example_obj.get_abs())
#     else:
#         form = ExampleForm()
#     return render(
#         request,
#         'app1/create.html',
#         {'form': form}
#     )

###################
# Class-based Views
###################
class Mixins:

    @classmethod
    def get_abs_url(self, uri, key, value):
        return reverse(uri, kwargs={key: value})


class ExampleDetail(View):
    examples_all = Example.objects.all()

    def get(self, request, slug=None):
        example_obj = get_object_or_404(Example, slug=slug)
        context = {
            'example_obj': example_obj,
            'request': request,
            'examples': self.examples_all
        }
        return render(
            request,
            'app1/example.html',
            context
        )


class ExampleCreate(RedirectView, Mixins):
    form_class = ExampleForm
    template_name = 'app1/create.html'
    context = {
        'form': form_class(),
        'examples': Example.objects.all()
    }

    def get(self, request, *args, **kwargs):
        return render(
            request,
            self.template_name,
            self.context
        )

    def post(self, request, *args, **kwargs):
        bound_form = self.form_class(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(self.get_abs_url('app1:oexample', 'slug', new_obj.slug)) # TODO: Fix redirection
        return render(
            request,
            self.template_name,
            self.context
        )


# View for single static test-page; no db orm queries, no dynamic data
class Boot(View):
    def get(self, request):
        return render(request, 'app1/btutorial.html')


###########################
# Generic Class-based Views
###########################
class ExampleDetailGeneric(DetailView):
    model = Example
    template_name = 'app1/example.html'