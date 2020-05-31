# Create your views here.
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Contacts
from django.urls import reverse
from django.http import HttpResponseRedirect

# def index(request):
#   return HttpResponse('hello world!') # in order to see hello world I needed to use the following URL: http://localhost:8000/contacts/index/


def index(request):
    # I need to import model in the view in order to access it = from .models import Contacts
    contacts = Contacts.objects.order_by('last_name')
    context = {
        'contacts': contacts  # this is a dictionary of contacts with the key contacts

        # 'message': 'Hello World!!'
    }
    # contacts will link with index.html with is going to connect to the detail page from the index.html
    return render(request, 'contacts/index.html', context)
    # this for loop will loop for each contact in contacts {% for contact in contacts %} then with the following div we are connecting to the detail page which I ordered by last name first name: <a href="{% url 'contacts:detail' contact.id %}"> {{contact.last_name}}, {{contact.first_name}} </a>

# View for the Detail


def detail(request, contact_id):
    contact = get_object_or_404(Contacts, pk=contact_id)
    return render(request, 'contacts/detail.html', {'contact': contact})
    # return HttpResponseRedirect(reverse('contacts:detail', args=(contact.id,))) # remember to putting a comma at the end

# create a view for new contact page


def create_contact(request):
    return render(request, 'contacts/contact_new.html')
