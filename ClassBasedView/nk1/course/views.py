from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def addition(request):
    list1=[1,2,3]
    list2=[4,4,6]
    list=list1 + list2

    return HttpResponse(list)