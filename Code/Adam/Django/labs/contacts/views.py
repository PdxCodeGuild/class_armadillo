from django.shortcuts import render
from django.http import HttpResponse

from .models import Contact

def base(request):
    return render(request, 'contacts/base.html')


def index(request):

    contacts = Contact.objects.all().order_by('last_name')
    # print(contacts)
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/index.html', context)


def detail(request, contact_id):
    return HttpResponse('detail page for contact with id ' + str(contact_id))


def new(request):
    return HttpResponse('new contact page')


def new_save(request):
    return HttpResponse('save contact')