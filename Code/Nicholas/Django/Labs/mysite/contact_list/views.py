from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Contact
from django.template import loader

def index(request):
    contact_lists = Contact.objects.order_by('last_name')
    template = loader.get_template('contact_list/index.html')
    context = {
        'contact_lists': contact_lists,
    }
    return HttpResponse(template.render(context, request))


def detail(request, contact_id):  
    contact = get_object_or_404(Contact, pk=contact_id)  
    return render(request, 'contact_list/detail.html', {'contact': contact})


