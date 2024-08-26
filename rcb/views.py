from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h1><marquee>virat is good cricketer</marquee></h1>')

def virat(request):
    return render(request,'sam.html')
