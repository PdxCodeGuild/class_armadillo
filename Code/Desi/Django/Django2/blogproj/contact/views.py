from django.shortcuts import render
from django.http import HttpResponse

# from django.http import HttpResponse

def index(request):

  page = request.GET.get('page', 1)

  contact = contact.objects.all().order_by['last_name']
  search = ''
  if request.method =='POST':
    search = request.POST['search']
    contact = contact.filter(Q(first_name_icontains=search)
                          |  Q(last_name_icontains=search)
                          |  Q(email_icontains=search)
                          |  Q(phone_number_icontains=search)
                          |  Q(comments_icontains=search))
                            
  context = {
    "contact": contact,
  }
  return HttpResponse('hello world!')
  return render(request, 'contact/index.html',)
