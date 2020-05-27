from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {
        'message': 'Hello World!'
    }
    return render(request, 'contacts/index.html', context)
