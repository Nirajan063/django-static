from django.shortcuts import render
from django.http import HttpResponse
from .forms import CountryForm, ProvinceForm
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


def add_country(request):
    add_country_form = CountryForm()
    context={
        "form": add_country_form,
        "title": "country | Add page"
    }
    return render(request,"add_country.html", context)



def provience(request):
    context={
        "province_name":"provience no. one",
        "province_code":"koshi",

    }
    return render(request,"provience.html",context)



def add_province(request):
    add_province_form = ProvinceForm()
    context={
        "form": add_province_form,
        "title": "province | Add pa=ge"
    }
    return render(request,"add_provience.html",context)
