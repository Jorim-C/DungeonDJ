# from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse("hello wold! i'm home.")
    return render(request,'home.html')

def about(request):
    # return HttpResponse("blaurgh")
    return render(request, 'about.html')