from django.shortcuts import render, get_object_or_404
from .models import Contact

from .forms import ContactForm

def index(request):
    contacts = Contact.objects.order_by('name')
    context = {
        'contacts': contacts
    }
    return render(request, 'main/index.html', context)

def create_contact(request):
    message = ''
    if request.method == 'POST':
        print(request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            form = ContactForm()
        else:
            message = 'form is not valid'
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'main/create_contact.html', context)

def create_contact_bootstrap(request):
    form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'main/create_contact_bootstrap.html', context)

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    if request.method == 'POST':
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm(instance=contact)
    context = {
        'form': form
    }
    return render(request, 'main/edit_contact.html', context)
