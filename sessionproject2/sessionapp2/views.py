from django.shortcuts import render
from sessionapp2.forms import additemform

# Create your views here.
def additemview(request):
    form=additemform()
    if request.method=='POST':
        name=request.POST['name']
        quantity=request.POST['quantity']
        request.session[name]=quantity
    return render(request,'sessionapp2/home.html',{'form':form})

def displayitemview(request):
    return render(request,'sessionapp2/display.html')