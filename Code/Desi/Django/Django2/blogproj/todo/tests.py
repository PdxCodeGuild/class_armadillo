from django.test import TestCase

from django.http import HttpResponse
# Create your tests here.
def index(request):
    return HttpResponse('Hello World!')

    