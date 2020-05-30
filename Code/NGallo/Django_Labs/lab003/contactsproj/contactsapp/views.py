from django.shortcuts import render

from .models import Contact



def index(request):
    contacts = Contact.objects.order_by('last_name')

    context = {
        'contacts': contacts,
    }

    return render(request, 'contactsapp/index.html', context)