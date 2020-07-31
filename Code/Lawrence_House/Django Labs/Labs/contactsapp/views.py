from django.shortcuts import render, get_object_or_404, reverse
from .models import Contact
from django.http import Http404, HttpResponse, HttpResponseRedirect
from datetime import datetime

# Create your views here.

def index(request):
    contacts = Contact.objects.order_by('first_name')
    context = {
        'title': 'List of Contacts',
        'contact': contacts
    }
    return render(request, 'contactsapp/index.html', context)

def detail(request, id):
    contact = Contact.objects.get(id = id)
    context = {
        'person': contact,
    }
    return render(request, 'contactsapp/detail.html', context)

def contactsnew(request):
    return render(request, 'contactsapp/newcontact.html')

def new_submit(request):
    print(request.POST)

    # Assigning POST data to variables

    contact_first_name = request.POST['contact_first_name']
    contact_last_name = request.POST['contact_last_name']
    contact_age = request.POST['contact_age']
    contact_birthday = request.POST['contact_birthday']
    contact_phone_number = request.POST['contact_phone_number']
    contact_is_cell = 'contact_is_cell' in request.POST
    contact_comments = request.POST['contact_comments']

    # Assigning variables to model fields and saving to database

    contact = Contact(  first_name = contact_first_name,
                        last_name = contact_last_name,
                        age = contact_age,
                        birthday = contact_birthday,                    
                        phone_number = contact_phone_number,
                        is_cell = contact_is_cell,
                        comments = contact_comments)
    contact.save()

    return HttpResponseRedirect(reverse('contactsapp:detail', args=[contact.id]))
