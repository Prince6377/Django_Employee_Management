from django.http import HttpResponse 
from django.shortcuts import render
import datetime

def home(request):
    print("Methos Call From Views")
    # return HttpResponse("<h1>Hellow Welcome Our Website </h1> ") 
    return render(request,"home.html",{})

def about(request):
    date=datetime.datetime.now()
    # return HttpResponse(date)
    return render(request,"about.html",{})