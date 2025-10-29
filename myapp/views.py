from django.shortcuts import render
from django.http import HttpResponse

def hello(request):
    return render(request, 'hello.html')

def section1(request):
    return render(request, 'section1.html')

def section2(request):
    return render(request, 'section2.html')

def section3(request):
    return render(request, 'section3.html')
