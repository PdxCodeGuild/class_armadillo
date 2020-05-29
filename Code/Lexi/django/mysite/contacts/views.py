from django.http import HttpResponse
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

    
def upload_image(request):
    my_image = request.FILES['my_image']
    model = MyModel(..., my_image=my_image)
    model.save()