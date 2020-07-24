from django.shortcuts import render

# Create an index view
from django.http import HttpResponse

def base(request):
    return render(request, 'contacts/base.html')


def index(request):
    context = {}
    return render(request, 'contacts/index.html', context)