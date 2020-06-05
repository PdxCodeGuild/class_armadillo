from django.shortcuts import render, redirect
from .models import  ShortenedURL
import string
import random

# Create your views here.
def index(request):
    if request.method == 'POST':
        url = request.POST['url']
        code = hash_gen()
        ShortenedURL.objects.create(url=url, code=code)

    context = {
        'short_urls': ShortenedURL.objects.all(),
    }

    return render(request, 'url_shortcut/index.html', context)

def redirect_url(request, code):
    url = ShortenedURL.objects.get(code=code)
    url.counter += 1
    url.save()
    return redirect(url.url)

#  done
def hash_gen():
    # string.printable
    hashed_url = ''
    for i in range(5):
        letter = random.choice(string.printable)
        if letter not in ['/', '\\', '?', ' ']:
            hashed_url += letter
        else:
            i -= 1
    return hashed_url

