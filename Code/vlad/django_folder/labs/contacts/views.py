# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from .models import Contacts

# def index(request):
#   return HttpResponse('hello world!') # in order to see hello world I needed to use the following URL: http://localhost:8000/contacts/index/


def index(request):
  contacts = Contacts.objects.order_by('last_name') # I need to import model in the view in order to access it = from .models import Contacts
  context = {
      'contacts': contacts

        #'message': 'Hello World!!'
    }
  return render(request, 'contacts/index.html', context)