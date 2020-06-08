from django.shortcuts import render

# Create your views here.
def login_page(request):
    return render(request, 'users/login.html')

def register_page(request):
    message = ''
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['password']
        if password != retype_password:
            message = 'password invalid'
            return render(request, 'users/register.html', {'message':message})
        if user.objects.filter(username=username).exists():
            message = 'a user exists with those creds'
            return render(request, 'users/register.html', {'message':message})
        user = Users.get_or_create
    return render(request, 'user/register.html')