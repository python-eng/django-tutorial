from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Myfees(request):
    return HttpResponse('My fees is High')