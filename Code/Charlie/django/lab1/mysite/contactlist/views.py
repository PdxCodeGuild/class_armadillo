from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.urls import reverse
from .models import Contact
from .forms import ContactForm

def create_contact(request):
    template = "create_contact.html"

    if request.method == "POST":
        form = ContactForm(request.POST)

        if form.is_valid():
            form.save()
            contact_details = Contact.objects.latest('id')
            return HttpResponseRedirect(reverse('contactlist:details', args=(contact_details.id,)))

    else:
        form = ContactForm()

    context = {"form": form,}

    return render(request, template, context)


def contacts(request):
    context = {"Contacts": Contact.objects.order_by('last_name')}
    return render(request, 'contact.html', context)


def details(request, id):
    contact_details = Contact.objects.get(pk=id)
    context = {
        "contact_details": contact_details,
    }
    return render(request, 'detail.html', context)


def update(request, id):
    contact_details = Contact.objects.get(pk=id)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact_details)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('contactlist:detail', args=(contact_details.id,)))
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
    return render(request, 'update_contact.html', context)