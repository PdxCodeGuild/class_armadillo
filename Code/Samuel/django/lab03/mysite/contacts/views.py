from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .models import Contact

def index(request):
    list_of_contacts = Contact.objects.order_by('first_name')
    template = loader.get_template('contacts/index.html')
    context = {
        'list_of_contacts': list_of_contacts,
    }
    return HttpResponse(template.render(context, request))

def contacts(request):
    return HttpResponse("Test")

def contacts_id(request, contacts_id):
    single_contact = Contact.objects.filter(pk=contacts_id).first()
    template = loader.get_template('contacts/contact.html')
    context = {
        'single_contact': single_contact,
    }
    return HttpResponse(template.render(context, request))

def contacts_new(request):
    new_contact = Contact()
    context = {
        'new_contact': new_contact,
    }
    return render(request, 'contacts/new.html', context)

def contacts_new_submit(request):
    print(request.POST)
    cell = 'is_cell' in request.POST
    new_contact = Contact(first_name = request.POST['first_name'], last_name = request.POST['last_name'], age = request.POST['age'], birthday = request.POST['birthday'], phone_number = request.POST['phone_number'], is_cell = cell, comments = request.POST['comments'])
    new_contact.save()
    return HttpResponseRedirect(reverse('contacts:contacts_id', args=(new_contact.id,)))