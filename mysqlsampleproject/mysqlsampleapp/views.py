from django.shortcuts import render
from mysqlsampleapp.models import hydjobs
from django.http import HttpResponse

# Create your views here.
def hydjobsview(request):
    hyd_jobs_list = hydjobs.objects.all()
    hydjobs_dict = {'hyd_jobs_list': hyd_jobs_list}
    return render(request,'mysqlsampleapp/sample.html',context=hydjobs_dict)