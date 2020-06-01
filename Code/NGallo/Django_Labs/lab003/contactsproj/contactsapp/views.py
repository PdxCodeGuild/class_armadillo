from django.shortcuts import render
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse
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
    
    return render(request, 'contactsapp/detail.html',context)

def addnew(request):
    context = { }
    return render(request, 'contactsapp/addnew.html', context)

def submit_form(request):

    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    birthday = request.POST['birthday']
    phone_number = request.POST['phone_number']
    is_cell = 'is_cell' in request.POST
    comment = request.POST['comment']

    contact = Contact.objects.create(first_name = first_name, 
        last_name = last_name,
        age = age,
        birthday = birthday,
        phone_number = phone_number,
        is_cell = is_cell,
        comment = comment,      
    )

    return HttpResponseRedirect(reverse('contactsapp:detail', args=(contact.id,)))