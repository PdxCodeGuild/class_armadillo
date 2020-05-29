from django.shortcuts import render

# Create your views here.

def index(request):
    contacts = contact.objects.order_by('first_name')
    context = {
        'title': 'Contact List',
        'contacts': contacts
    }
    return render(request, 'contactsapp/index.html', context)

# def contacts(request):
#     return render(request, 'contactsapp/contacts.html')

# def contactsid():

# def contactsnew():

# def contactsnewsubmit()

