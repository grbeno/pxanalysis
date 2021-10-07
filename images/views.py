from django.shortcuts import render
from django.http import HttpResponse

def firstTest(request):
    return HttpResponse('Test: Hello Px!')
