from django.shortcuts import render, get_object_or_404
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
    contact = get_object_or_404(Contact, id=contact_id)
    context = {
        'contact': contact
    }
    return render(request, 'contacts/detail.html', context)


def new(request):
    return render(request, 'contacts/new.html')


def new_save(request):
    return HttpResponse('save contact')