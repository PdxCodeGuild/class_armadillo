from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Contacts
# Create your views here.


def index(request):
    contacts = Contacts.objects.all()
    return render(request, 'contacts/index.html', {'contacts': contacts})

def add(request):
    return render(request, 'contacts/add.html')

def save(request):
    first_name = request.POST['First Name']
    last_name = request.POST['Last Name']
    age = request.POST['Age']
    birthday = request.POST['Birthday']
    phone_number = request.POST['Phone Number']
    is_cell = request.POST['Cell']
    comments = request.POST['Comments']
    
    contacts = Contacts(
        First_Name = first_name,
        Last_Name = last_name,
        Age= age,
        Birthday = birthday,
        Phone_Number = phone_number,
        Cell = is_cell,
        Comments = comments

    )
    contacts.save()

    return HttpResponseRedirect(reverse('Contacts:index'))

