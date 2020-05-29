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

    else:
        form = ContactForm()

    context = {"form": form,}

    return render(request, template, context)


def contacts(request):
    context = {"Contacts": Contact.objects.order_by('last_name')}
    return render(request, 'contacts.html', context)


def details(request, id):
    contact_details = Contact.objects.get(pk=id)
    context = {
        "contact_details": contact_details,
        # 'First Name': contact_details.first_name,
        # 'Last Name': contact_details.last_name,
        # 'Age': contact_details.age,
        # 'Birthday': contact_details.birthday,
        # 'Email': contact_details.email,
        # 'Phone Number': contact_details.phone_number,
        # 'Cell': contact_details.is_cell,
        # 'Description': contact_details.comments,
    }
    print(context)
    return render(request, 'details.html', context)