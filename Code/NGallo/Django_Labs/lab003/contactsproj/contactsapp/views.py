from django.shortcuts import render
from django.http import Http404
from .models import Contact



def index(request):
    contacts = Contact.objects.order_by('last_name')

    context = {
        'contacts': contacts,
    }

    return render(request, 'contactsapp/index.html', context)

def detail(request, contact_id):
    try:
        contact = Contact.objects.get(pk=contact_id)
    except Contact.DoesNotExist:
        raise Http404("Contact does not exist")    
    
    
    context = {'contact': contact}
    
    return render(request, 'contactsapp/detail.html' ,context)
