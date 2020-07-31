from django.shortcuts import render, reverse
import django.contrib.auth
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import User
import requests
from . import secrets


def register(request):
    # print(request.method)
    if request.method == 'POST': # receiving a form submission

        # recaptcha bit
        recaptcha_response = request.POST['g-recaptcha-response']
        response = requests.post('https://www.google.com/recaptcha/api/siteverify', data={
            'secret': secrets.recaptcha_secret_key,
            'response': recaptcha_response
        })
        recaptcha_response_data = response.json()
        if not recaptcha_response_data['success']:
            return render(request, 'users/register.html', {'warning': 'Bad recaptcha!'})
        
        # create a user
        print(request.POST)
        username = request.POST['username']
        email = request.POST['email']
        phone_number = request.POST['phone_number']
        password = request.POST['password']
        retype_password = request.POST['retype_password']

        if password != retype_password:
            return render(request, 'users/register.html', {'warning': 'Your passwords don\'t match!'})
        # if User.objects.filter(username=username).count() > 0:
        if User.objects.filter(username=username).exists():
            return render(request, 'users/register.html', {'warning': 'A user already exists with that username'})
        
        user = User.objects.create_user(username, email, password)
        user.phone_number = phone_number
        user.save()

        django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('main:list'))

    return render(request, 'users/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = django.contrib.auth.authenticate(request, username=username, password=password)
        if user is None:
            return render(request, 'users/login.html', {'warning': 'Username and password do not match!'})
        django.contrib.auth.login(request, user)
        return HttpResponseRedirect(reverse('main:list'))
    return render(request, 'users/login.html')


def logout(request):
    django.contrib.auth.logout(request)
    return HttpResponseRedirect(reverse('users:login'))

@login_required
def profile(request):
    return render(request, 'users/profile.html')
