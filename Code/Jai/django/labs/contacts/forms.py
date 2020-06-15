from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact

        fields= [ 
            'first_name',
            'last_name',
            'age',
            'birthday',
            'phone_number',
            #'comments',
            "is_cell"

        ]


