from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

def index(request):
    contact_lists = Contact.objects.all()
    context = {
        'contact_lists': contact_lists
    }
    return render(request, 'contact_list/index.html', context)

