from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def string1(request):
    return HttpResponse('<h1>2 app 1 fun first 1 vieww</h1>')

def string2(request):
    return HttpResponse('<h1>2 app 2nd fun 2 vieww</h1>')