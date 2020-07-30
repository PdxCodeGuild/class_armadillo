from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect

from .models import Contact


def base(request):
    return render(request, 'contacts/base.html')


def index(request):

    contacts = Contact.objects.all().order_by('last_name')
    # print(contacts)
    context = {
        'contacts': contacts
    }
    return render(request, 'contacts/index.html', context)


def detail(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    context = {
        'contact': contact
    }
    return render(request, 'contacts/detail.html', context)


def new(request):
    return render(request, 'contacts/new.html')


def new_save(request):
    print(request.POST)
    contact_first_name = request.POST['contact_first_name']
    contact_last_name = request.POST['contact_last_name']
    contact_birthday = request.POST['contact_birthday']
    contact_phone_number = request.POST['contact_phone_number']
    contact_is_cell = 'contact_is_cell' in request.POST
    contact_comments = request.POST['contact_comments']

    contact = Contact(first_name=contact_first_name,
                      last_name=contact_last_name,
                      birthday=contact_birthday,
                      phone_number=contact_phone_number,
                      is_cell=contact_is_cell,
                      comment=contact_comments)

    contact.save()

    return HttpResponseRedirect(reverse('contacts:detail', args=[contact.id,]))
