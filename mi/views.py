from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def ro(request):
    return HttpResponse('<h1><marquee>ro is hitman of ceicket</marquee></h1>')

def rohit(request):
    return render(request,'sam.html')
