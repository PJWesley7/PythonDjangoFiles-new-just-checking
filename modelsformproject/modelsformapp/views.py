from django.shortcuts import render
from modelsformapp import forms

# Create your views here.
def studentview(request):
    form = forms.studentForm()
    if request.method=='POST':
        form=forms.studentForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            print("Form inserted into database successfully")
    return render(request,'modelsformapp/modelsformapp.html',{'form':form})
