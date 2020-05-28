from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

def index(request):
    contact_lists = Contact.objects.all()
    context = {
        'contact_lists': contact_lists
    }
    return render(request, 'contact_list/index.html', context)



def detail(request, contact_id):  
    contact = get_object_or_404(Contact, pk=contact_id)  
    if not post.approved:
        raise Http404
    return render(request, 'contact_list.detail.html', {'contact': contact})
