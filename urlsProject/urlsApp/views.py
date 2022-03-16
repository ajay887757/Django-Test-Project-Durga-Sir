from django.shortcuts import render
from django.http import HttpResponse

def hydjobsInfo(request):
    s='<h1>hydrabad Jobs Informations</h1>'
    return HttpResponse(s)
def punejobsInfo(request):
    s='<h1>pune Jobs Informations</h1>'
    return HttpResponse(s)
def mumbaijobsInfo(request):
    s='<h1>mumbai Jobs Informations</h1>'
    return HttpResponse(s)
def noidajobsInfo(request):
    s='<h1>noida Jobs Informations</h1>'
    return HttpResponse(s)



