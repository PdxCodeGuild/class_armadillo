from django.shortcuts import render, get_object_or_404, reverse
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseRedirect
import string
from django.db.models import Q
from datetime import datetime

from .models import Contact

def index(request):
    # print(request.POST)

    # get value of 'page' from the query string, default to 1 if the query parameter is not specified
    page = request.GET.get('page', 1)
    

    contacts = Contact.objects.all().order_by('last_name')
    search = ''
    if request.method == 'POST':
        # print(request.POST)
        search = request.POST['search_text']
        # contacts = contacts.filter(last_name__icontains=search)
        contacts = contacts.filter(Q(first_name__icontains=search)
                                | Q(last_name__icontains=search)
                                | Q(email__icontains=search)
                                | Q(phone_number__icontains=search)
                                | Q(comments__icontains=search))
    paginator = Paginator(contacts, 10)
    contacts = paginator.page(page)
    context = {
        'contacts': contacts,
        'search': search
    }
    return render(request, 'contacts/index.html', context)


def detail(request, contact_id):
    # return HttpResponse('detail page for contact with id ' + str(contact_id))
    # contact = Contact.objects.get(id=contact_id)
    contact = get_object_or_404(Contact, id=contact_id)

    context = {
        'contact': contact
    }
    return render(request, 'contacts/detail.html', context)

def new(request):
    return render(request, 'contacts/new.html')

def new_submit(request):
    print(request.POST) # dictionary containing our form data

    contact_first_name = request.POST['contact_first_name']
    contact_last_name = request.POST['contact_last_name']
    contact_first_name = request.POST['contact_first_name']

    contact_birthday = request.POST['contact_birthday']
    # parse the birthday from a string into a datetime object - optional
    contact_birthday = datetime.strptime(contact_birthday, '%Y-%m-%d').date()

    contact_email = request.POST['contact_email']
    contact_phone_number = request.POST['contact_phone_number']
    contact_phone_number = ''.join([char for char in contact_phone_number if char in string.digits])
    # phone_number = ''
    # for char in contact_phone_number:
    #     if char in string.digits:
    #         phone_number += char
    # contact_phone_number = phone_number

    # contact_is_cell = request.POST['contact_is_cell']
    contact_is_cell = 'contact_is_cell' in request.POST
    contact_comments = request.POST['contact_comments']

    contact = Contact(first_name = contact_first_name,
                        last_name = contact_last_name,
                        birthday = contact_birthday,
                        email = contact_email,
                        phone_number = contact_phone_number,
                        is_cell = contact_is_cell,
                        comments = contact_comments)
    contact.save()

    # return HttpResponseRedirect(reverse('contacts:index'))
    return HttpResponseRedirect(reverse('contacts:detail', args=[contact.id]))


def delete(request, contact_id):
    contact = Contact.objects.get(id=contact_id)
    contact.delete()
    return HttpResponseRedirect(reverse('contacts:index'))


def edit(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    context = {
        'contact': contact
    }
    return render(request, 'contacts/edit.html', context)

def edit_submit(request):

    # get the form data out of request.POST
    contact_id = request.POST['contact_id']
    contact_first_name = request.POST['contact_first_name']
    contact_last_name = request.POST['contact_last_name']
    contact_first_name = request.POST['contact_first_name']

    contact_birthday = request.POST['contact_birthday']
    # parse the birthday from a string into a datetime object - optional
    contact_birthday = datetime.strptime(contact_birthday, '%Y-%m-%d').date()

    contact_email = request.POST['contact_email']
    contact_phone_number = request.POST['contact_phone_number']
    # remove any non-digit characters
    contact_phone_number = ''.join([char for char in contact_phone_number if char in string.digits])
    
    contact_is_cell = 'contact_is_cell' in request.POST
    contact_comments = request.POST['contact_comments']

    # get the contact we're editing
    contact = Contact.objects.get(id=contact_id)

    # assign values to the properties of our contact
    contact.first_name = contact_first_name
    contact.last_name = contact_last_name
    contact.birthday = contact_birthday
    contact.email = contact_email
    contact.phone_number = contact_phone_number
    contact.is_cell = contact_is_cell
    contact.comments = contact_comments

    # save our contact
    contact.save()

    # redirect to the detail page for the contact
    return HttpResponseRedirect(reverse('contacts:detail', args=[contact.id]))