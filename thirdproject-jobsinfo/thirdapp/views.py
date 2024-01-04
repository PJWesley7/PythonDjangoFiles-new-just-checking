from django.shortcuts import render
from django.http import HttpResponse

def hydjobs(request):
    hjobs = '<h1>The info for hyd jobs</h1>'
    return HttpResponse(hjobs)

def chennaijobs(request):
    hjobs = '<h1>The info for chennai jobs</h1>'
    return HttpResponse(hjobs)

def mumbaijobs(request):
    hjobs = '<h1>The info for mumbai jobs</h1>'
    return HttpResponse(hjobs)

def bangalorejobs(request):
    hjobs = '<h1>The info for bangalore jobs</h1>'
    return HttpResponse(hjobs)
