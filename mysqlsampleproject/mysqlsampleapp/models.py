from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)

class blorejobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)

class punejobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)

class chennaijobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    email = models.EmailField()
    phonenumber = models.CharField(max_length=10)