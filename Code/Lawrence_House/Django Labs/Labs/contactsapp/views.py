from django.shortcuts import render, get_object_or_404, reverse
from .models import Contact
from django.http import Http404, HttpResponse, HttpResponseRedirect

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
    context = {}

    return render(request, 'contactsapp/newcontact.html', context)

# def contactsnewsubmit():
#     print(request.POST) #form data in dict
#     contact_first_name = request.POST['contact_first_name']
#     contact_last_name = request.POST['contact_last_name']
#     contact_birthday = request.POST['contact_birthday']
#     contact_email = request.POST['contact_email']
#     contact_phone_number = request.POST['contact_phone_number']
#     return HttpResponse('save contact')
