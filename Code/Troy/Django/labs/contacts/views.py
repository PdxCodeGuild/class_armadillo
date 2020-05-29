from django.shortcuts import render
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
        # return HttpResponseRedirect(request, 'contacts/index.html', context)
    return render(request, 'contacts/detail.html')
    
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

    return HttpResponseRedirect(reverse('contacts:index'))
