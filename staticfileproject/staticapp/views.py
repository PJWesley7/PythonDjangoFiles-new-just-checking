from django.shortcuts import render
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates\\staticapp')

# Create your views here.
def home(request):
    return render(request,f'{TEMPLATE_DIR}\index.html')

def profile(request):
    return render(request,f'{TEMPLATE_DIR}\profile.html')