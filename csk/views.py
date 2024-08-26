from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def msd(request):
    return HttpResponse('<h1><marquee>Dhoni is a good wicketkeeper</marquee></h1>')

def mahi(request):
    return render(request,'sam.html')
