from django import forms
from .models import contact
from django.db import models
from django.forms import ModelForm

class DateInput(forms.DateInput):
    input_type = 'date'

class contactform(forms.ModelForm):
    class Meta:
        model = contact
        fields = ('first_name', 'last_name', 'age', 'birthday', 'telephone', 'email', 'message')
        widgets = {
            'birthday': DateInput(attrs={'type': 'date'}),
        }