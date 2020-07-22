
from django import forms
from .models import Contact

class DateInput(forms.DateInput):
    input_type = 'date'

class ContactForm(forms.ModelForm):
    class Meta:
        # the model to associate with the form
        model = Contact
        # a list of all the models' fields you want in the form
        # fields = ['name', 'student_id', 'birthday']
        # or just use all of them
        fields = '__all__'

        widgets = {
            'birthday': DateInput()
        }