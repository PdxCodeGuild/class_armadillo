from django.shortcuts import render
from .forms import contactform



def contact(request):
    template = "contact.html"
    
    if request.method == 'POST':
        form = contactform(request.POST)

        if form.is_valid():
            form.save()
    else:
        form = contactform()


    context = {
        'form': form,
    }
    return render(request, template, context)
# Create your views here.
