from landing.models import Person
from django.forms import ModelForm

from django import forms


class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ['fisrt_name', 'last_name', 'company', 'your_role', 'email', 'comment']

        widgets = {
            "email": forms.EmailInput(attrs={'class': 'validate', 'placeholder': ' '}),
            "last_name": forms.TextInput(attrs={'class': 'validate', 'placeholder': ' '}),
            "fisrt_name": forms.TextInput(attrs={'class': 'validate', 'placeholder': ' '}),
            "company": forms.TextInput(attrs={'class': 'validate', 'placeholder': ' '}),
            "your_role": forms.TextInput(attrs={'class': 'validate', 'placeholder': ' '}),
            "comment": forms.Textarea(attrs={'class': 'materialize-textarea', 'placeholder': ' '}),
        }

        labels = {
            'comment': ('Comment (optional)'),
        }
