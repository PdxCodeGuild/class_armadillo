from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Contact

def index(request):

    contacts = Contact.objects.all()
    
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/index.html', context)


def details(request, contact_id):
    # return HttpResponse('detail page for contact with id' + str(contact_id))
    contact = Contact.objects.get(id=contact_id)
    context = {
        'contact': contact
    }
    return render(request, 'contacts/details.html', context)

def new(request):
    context = {}
    return render(request, 'contacts/new.html', context)

def save_submit(request):
    print(request.POST)
    contact_first_name = request.POST['contact_first_name']
    contact_last_name = request.POST['contact_last_name']
    contact_birthday = request.POST['contact_birthday']
    contact_phone_number = request.POST['contact_phone_number']
    contact_comments = request.POST['contact_comments']
    
    contact = Contact(
        first_name = contact_first_name,
        last_name = contact_last_name,
        birthday = contact_birthday,
        phone_number = contact_phone_number,
        comments = contact_comments,
    )
    contact.save()

    # return HttpResponse('Contact saved')
    