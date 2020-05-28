from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Contacts
# Create your views here.


def index(request):
    contacts = Contacts.objects.all()
    return render(request, 'contacts/index.html', {'contacts': contacts})