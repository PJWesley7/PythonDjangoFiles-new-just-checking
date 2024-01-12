from django.shortcuts import render
from sessionapp.forms import nameform,ageform,gfform
# Create your views here.
def name_view(request):
    form = nameform()
    return render(request,'sessionapp/nameform.html',{'form':form})

def age_view(request):
    name= request.GET['name']
    request.session['name'] = name
    form= ageform()
    return render(request,'sessionapp/ageform.html',{'form':form})

def gf_view(request):
    age= request.GET['age']
    request.session['age'] = age
    form= gfform()
    return render(request,'sessionapp/gfform.html',{'form':form})