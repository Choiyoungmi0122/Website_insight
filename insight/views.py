from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

from django.http import HttpResponse

context = {}

def index(request):
    return render(request, 'insight home.html')

