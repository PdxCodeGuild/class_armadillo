from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Contact
from .forms import ContactForm, ContactDeleteForm

# Create your views here.

def index(request):
    context = {        
        'contacts': Contact.objects.all()

    }
    return render(request, 'index.html', context)


def create(request):
    context = {}
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form.save()
        print('saved, redirecting')
        return redirect('index')
    context['form'] = form

    return render(request, 'new.html', context)

def detail(request, id):
    context = {'contact': Contact.objects.get(id = id)} 
    return render(request, 'detail.html', context)


def delete(request, pk=None):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = DeleteForm(request.POST, instance= contact)
        
        if form.is_valid():
            contact.delete()
            return redirect('create')

    else:
        form - DeleteForm(instance= contact)
        
    return render(request, 'contact/delete')



'''
The application will have the following views:

- `/contacts/` will render a template containing a `new contact` button, as well as a list of contacts each with a `view contact` button
- `/contacts/<id>/` will be a detail page for a contact with the given `id`
- `/contacts/new/` will render a template containing a form for creating a new contact
- `/contacts/new/submit/` will receive the form submission from `/contacts/new/`, create a new contact in the database, and redirect to the detail page for the newly created contact
'''