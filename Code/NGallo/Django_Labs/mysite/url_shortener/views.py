from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.template import loader
import random
import string
from .models import ShortenedURL
def index(request):
    urls = ShortenedURL.objects.all()
    context = {
        'urls': urls
    }
    return render(request, 'url_shortener/index.html', context)

def save(request):
    letters_to_make_string = string.ascii_letters+string.digits
    
    random_string = ""
    for i in range(6):
        random_string += random.choice(letters_to_make_string)
    # print(random_string)
    # print(request.POST)
    new_url = ShortenedURL(
    code=random_string,
    url = request.POST['shortened_url'],
    counter = 0
    )
    new_url.save()
    return HttpResponseRedirect(reverse('url_shortener:index'))

def redirect(request, code):
    shorten_url = ShortenedURL.objects.get(code=code)
    link = shorten_url.url
    shorten_url.counter += 1
    shorten_url.save()
    return HttpResponseRedirect(link)
