# fileupload/views.py

from django.shortcuts import render, redirect
from .models import UploadedFile
from .forms import FileUploadForm

def home(request):
    files = UploadedFile.objects.all()
    return render(request, 'awsfileuploadapp/home.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = FileUploadForm()
    return render(request, 'awsfileuploadapp/upload_file.html', {'form': form})
