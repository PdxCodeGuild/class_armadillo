from django.shortcuts import render

def index(request):

    return render(request, 'url_shortener/index.html')

def save(request):
    pass

def redirect(request):
    pass
