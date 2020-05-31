from django.http import HttpResponse, Http404
from django.shortcuts import render
from .models import Contact
from .models import MyModel


def index(request):
    contacts = Contact.objects.all()
    context = {
        'contacts' : contacts
    }
    print(contacts)
    return render(request, 'contacts/index.html', context)

# manticore img
def upload_image(request):
    my_image = request.FILES['my_image']
    model = MyModel(..., my_image=my_image)
    model.save()

# page to view contact details
def detail(request, contact_id):
    try:
        question = Contact.objects.get(pk=contact_id)
    except Contact.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, 'polls/detail.html', {'contact': contact})

# page to create a  new contact
def create_contact(request):
    contact_id = contact_id.objects.order_by('')