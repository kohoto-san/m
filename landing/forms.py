from landing.models import Person
from django.forms import ModelForm

from django import forms


class PersonForm(ModelForm):

    class Meta:
        model = Person
        fields = ['fisrt_name', 'last_name', 'company', 'person_role', 'email']

        widgets = {
            "email": forms.TextInput(attrs={'class': 'validate', 'type': 'email', 'placeholder': ' '}),
            "last_name": forms.TextInput(attrs={'class': 'validate', 'placeholder': ' '}),
            "fisrt_name": forms.TextInput(attrs={'class': 'validate', 'placeholder': ' '}),
            "company": forms.TextInput(attrs={'class': 'validate', 'placeholder': ' '}),
            "person_role": forms.TextInput(attrs={'class': 'validate', 'placeholder': ' '}),
        }
