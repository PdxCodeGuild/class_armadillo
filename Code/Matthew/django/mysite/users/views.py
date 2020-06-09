from django.shortcuts import render, reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


# if the user is not logged in, this redirects them to whatever path is in the settings.py as LOGIN_URL
# if the user is logged in, the view proceeds as usual
@login_required
def home(request):
    print(request.user.username)
    return render(request, 'users/home.html')

def login_page(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)
        if user is None: # username and password do not match, go back to the page
            return render(request, 'users/login.html', {'message': 'there is no user with that username and password'})
        # user was found, log them in and redirect to the home page
        login(request, user)
        # if there's a next parameter in the url e.g. localhost:8000/users/login/?next=/users/home/
        if 'next' in request.GET:
            return HttpResponseRedirect(request.GET['next'])
        return HttpResponseRedirect(reverse('users:home'))
        
    return render(request, 'users/login.html')

def register_page(request):
    if request.method == 'POST':
        
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        retype_password = request.POST['retype_password']

        if password != retype_password:
            return render(request, 'users/register.html', {'message': 'passwords do not match'})
        if User.objects.filter(username=username).exists(): # check if a user with that username already exists
            return render(request, 'users/register.html', {'message': 'a user with that username already exists'})
        # create the user, log them in, and redirect to the home page
        user = User.objects.create_user(username, email, password)
        login(request, user)
        return HttpResponseRedirect(reverse('users:home'))

    return render(request, 'users/register.html')


def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login_page'))