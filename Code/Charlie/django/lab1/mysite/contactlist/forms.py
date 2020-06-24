from django import forms
from .models import Contact
from django.forms import ModelForm


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('first_name', 'last_name', 'age', 'birthday', 'email', 'phone_number', 'is_cell', 'comments',)


class ContactDeleteForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name']