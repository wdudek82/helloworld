from django import forms
from django.utils import timezone

from .models import Example


class ExampleForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = [
            'name', 'flag', 'tag', 'slug']
            # 'created_at', 'published_at', 'updated_at',
        # ]
