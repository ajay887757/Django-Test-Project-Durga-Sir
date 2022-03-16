from django.shortcuts import render
from django.http import HttpResponse
import datetime


# Create your views here.
def Welcome(request):
    s="<h1>Welcome to the jungle</h1>"
    return HttpResponse(s)
def timeinfo(request):
    date= datetime.datetime.now()
    msg="<h1> Hello Friend Good Evening!!! </h1><hr>"
    msg=msg+"<h1> Now Server time is :"+str(date)+'</h1>'
    return HttpResponse(msg)
def hydjobs(request):
    s="hydrabad jon Info"
    return HttpResponse(s)
def Mumbaijobs(request):
    s="Mumbai jon Info"
    return HttpResponse(s)
def Biharjob(request):
    s="Bihar jon Info"
    return HttpResponse(s)
def Datetime(request):
    date=datetime.datetime.now()
    h=int(date.strftime("%H"))
    msg='<h1> Hello guest very'
    if h<12:
        msg=msg+"Good Morning"
    elif h<16:
        msg=msg+"Very Good Afternoon"
    elif h<21:
        msg=msg+"Very Good Evening"
    else:
        msg=msg+"Good Night"
    msg=msg+"</h1><hr>"
    msg=msg+"<h1>How the server time is :"+str(date)+"</h1>"
    return HttpResponse(msg)
