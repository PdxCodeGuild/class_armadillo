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

