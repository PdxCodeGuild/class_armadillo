from django.http import HttpResponse
from django.shortcuts import render
from .models import Contact


def index(request):
    contacts = Contact.objects.all()
    context = {
        'contacts' : contacts
    }
    print(contacts)
    return render(request, 'contacts/index.html', context)