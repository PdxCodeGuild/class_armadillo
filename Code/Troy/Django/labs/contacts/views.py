from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Contacts
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    contacts = Contacts.objects.all()

    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/index.html', context)

def detail(request, contact_id):
    contact = get_object_or_404(Contacts, pk=contact_id)
    return render(request, 'contacts/detail.html', {'contact':contact})

def new_contact_page(request):
    return render(request, 'contacts/new_contact.html')
    
def new_contact(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    birth_date = request.POST['birth_date']
    phone_number = request.POST['phone_number']
    is_cell = 'is_cell' in request.POST
    comments = request.POST['comments']
    new_contact = Contacts(first_name=first_name, 
        last_name=last_name, 
        age=age, 
        birth_date=birth_date,
        phone_number=phone_number, 
        is_cell=is_cell, 
        comments=comments)
    new_contact.save()

    return HttpResponseRedirect(reverse('contacts:detail', args=(new_contact.id,)))
