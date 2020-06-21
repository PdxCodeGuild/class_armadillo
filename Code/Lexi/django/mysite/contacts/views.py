from django.shortcuts import render, get_object_or_404, reverse
from .models import Contact
from django.urls import reverse
from django.http import HttpResponseRedirect

# view at main page
def index(request):
    contacts = Contact.objects.order_by('last_name')
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/index.html', context)

# view at details page
def detail(request, contact_id):
    # card = Contact.objects.get(pk=card_id)
    contacts = get_object_or_404(Contact, pk=contact_id)
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/detail.html', context)

# view at submitting contact page
def new_contact(request):
    return render(request, 'contacts/submit_contact.html')

# function for above page
def submit_contact(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    age = request.POST['age']
    birthday = request.POST['birthday']
    phone_number = request.POST['phone_number']
    is_cell = 'is_cell' in request.POST
    comments = request.POST['comments']
    new_contact = Contact(first_name=first_name, last_name=last_name, age=age,
        birthday=birthday, phone_number=phone_number, is_cell=is_cell, comments=comments)
    new_contact.save()
    return HttpResponseRedirect(reverse('contacts:detail', args=(new_contact.id,)))

# manticore img
def upload_image(request):
    my_image = request.FILES['my_image']
    model = MyModel(..., my_image=my_image)
    model.save()
