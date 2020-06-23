from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse
from .models import Contact
from .forms import ContactForm, ContactDeleteForm

def create_contact(request):
    template = "create_contact.html"

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            contact_details = Contact.objects.latest('id')
            return redirect(reverse('contactlist:details', args=(contact_details.id,)))

    else:
        form = ContactForm()

    context = {"form": form,}

    return render(request, template, context)


def contacts(request):
    context = {"Contacts": Contact.objects.order_by('last_name')}
    return render(request, 'contactlist/contacts.html', context)


def details(request, id):
    contact_details = Contact.objects.get(pk=id)
    context = {
        "contact_details": contact_details,
    }
    return render(request, 'contactlist/details.html', context)


def update(request, id):
    contact_details = Contact.objects.get(pk=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact_details)
        if form.is_valid():
            form.save()
            return redirect(reverse('contactlist/details', args=(contact_details.id,)))
    else:
        form = ContactForm(initial={"first_name": contact_details.first_name,
                                    "last_name": contact_details.last_name,
                                    "age": contact_details.age,
                                    "birthday": contact_details.birthday,
                                    "email": contact_details.email,
                                    "phone_number": contact_details.phone_number,
                                    "is_cell": contact_details.is_cell,
                                    "comments": contact_details.comments,
        })

    context = {
        "contact_details": contact_details,
        "form": form,
    }
    return render(request, 'contactlist/update_contact.html', context)

def delete(request, pk=None):
    contact = get_object_or_404(Contact, pk=pk)
    if request.method == "POST":
        form = DeleteForm(request.POST, instance= contact)
        
        if form.is_valid():
            contact.delete()
            return redirect('create')

    else:
        form - DeleteForm(instance= contact)
        
    return render(request, 'contactlist/contact/delete')