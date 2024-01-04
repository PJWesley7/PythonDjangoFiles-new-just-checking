from django.shortcuts import render
from pathlib import Path
import os
import datetime



date = datetime.datetime.now()
dict_date = {'date_msg':date}
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATE_DIR = os.path.join(BASE_DIR,'templates\\templatesProjectapp')

# Create your views here.
def tempview(request):
    return render(request,f'{TEMPLATE_DIR}\wish.html',context=dict_date)
