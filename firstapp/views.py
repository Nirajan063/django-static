from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def demo(request):
    #print ("Hello world")
    return HttpResponse("Hello! this is my first django")
def country(request):
    context ={
        "country_name":"Nepal", 
        "continent":"Asia",
        "country_code":"+977"

    }
    return render(request,"country.html",context)

def provience(request):
    context={
        "province_name":"provience no. one",
        "province_code":"koshi",

    }
    return render(request,"provience.html",context)
