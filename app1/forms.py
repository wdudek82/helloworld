from django import forms
from .models import Example
from django.utils import timezone

class ExampleForm(forms.ModelForm):
    class Meta:
        model = Example
        fields = [
            'name', 'flag', 'tag', 'slug']
            # 'created_at', 'published_at', 'updated_at',
        # ]
