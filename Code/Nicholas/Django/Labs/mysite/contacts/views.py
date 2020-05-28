from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact


def index(request):
    contacts = Contacts.objects.order_by('first_name')
    context = {
        'title': 'Contacts List',
        'contacts': 'Contacts'
    }
    return render(request, 'contacts/index.html', context)
