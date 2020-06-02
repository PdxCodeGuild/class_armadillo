from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.

def index(request):
    context = {        
        'contacts': contacts

    }
    return render(request, 'contacts/index.html', context)




## Views
'''
The application will have the following views:

- `/contacts/` will render a template containing a `new contact` button, as well as a list of contacts each with a `view contact` button
- `/contacts/<id>/` will be a detail page for a contact with the given `id`
- `/contacts/new/` will render a template containing a form for creating a new contact
- `/contacts/new/submit/` will receive the form submission from `/contacts/new/`, create a new contact in the database, and redirect to the detail page for the newly created contact
'''