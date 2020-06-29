from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
from django.template import loader
# Create your views here.

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

def new_contact(request):
    new_contact = Contact()
    context = {
        'new_contact': new_contact,
    }
    return render(request, 'contact_list/new_contact.html', context)

def submit(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    birthday = request.POST['birthday']
    phone_number = request.POST['phone_number']
    if 'is_cell' in request.POST:
        is_cell = True
    else:
        is_cell = False    
    comments = request.POST['comments']

    new_contact = Contact(first_name=first_name,
                          last_name=last_name,
                          age=age,
                          birthday=birthday,
                          phone_number=phone_number,
                          is_cell=is_cell,
                          comments=comments,)
    new_contact.save()

    return HttpResponseRedirect(reverse('contact_list:index'))