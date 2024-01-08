from django.shortcuts import render
from . import forms

# Create your views here.
def feedbackformview(request):
    form = forms.feedbackform()
    if request.method == 'POST':
        form = forms.feedbackform(request.POST)
        if form.is_valid():
            print('Form Validation success and printing feedback info')
            print('Student name:',form.cleaned_data['name'])
            print('Student name:',form.cleaned_data['rollno'])
            print('Student name:',form.cleaned_data['email'])
            print('Student name:',form.cleaned_data['feedback'])
            return render(request,'feedbackformapp/thankyou.html',{'name': form.cleaned_data['name']})
    return render(request,'feedbackformapp/feedbackform.html',{'form': form})





