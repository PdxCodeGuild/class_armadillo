# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Contacts
from django.urls import reverse
from django.http import HttpResponseRedirect

# def index(request):
#   return HttpResponse('hello world!') # in order to see hello world I needed to use the following URL: http://localhost:8000/contacts/index/


def index(request):
  contacts = Contacts.objects.order_by('last_name') # I need to import model in the view in order to access it = from .models import Contacts
  context = {
      'contacts': contacts

        #'message': 'Hello World!!'
    }
  return render(request, 'contacts/index.html', context)

def detail(request, contact_id):
  contact = get_object_or_404(Contacts, pk=contact_id)
  return render(request, 'contacts/detail.html', {'contact':contact})
  # return HttpResponseRedirect(reverse('contacts:detail', args=(contact.id,))) # remember to putting a comma at the end 

# # create a view for new contact page
# def create_contact(request):
#   return render(request, 'contacts/contact_new.html')