from django.shortcuts import render
from Sessionapp.form import Nameform,Age,Gf

# Create your views here.
def name_view(request):
    form=Nameform()
    return render (request,"name.html",{"form":form})


def age(request):
    name=request.GET['name']
    print(name)
    request.session['name']=name
    form=Age()
    return render(request,"age.html",{"form":form})

def gf(request):
    age=request.GET['age']
    print(age)
    request.session['age']=age
    form=Gf()
    return render(request,"gf.html",{"form":form})

def result(request):
    gf=request.GET['gf']
    print(gf)
    request.session['gf']=gf
    return render(request,"result.html")