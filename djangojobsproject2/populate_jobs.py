import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','djangojobsproject2.settings')
import django
django.setup()

from djangojobsapp2.models import *
from faker import Faker
from random import *
fake=Faker()

def phonenumbergen():
    d1 = randint(7, 9)
    num = '' + str(d1)
    for i in range(8):  # Change to 8 to ensure a total length of 10
        num = num + str(randint(0, 9))
    return num

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle= fake.job()
        feligibility= fake.random_element(elements=('Fresher', 'Experienced', 'Intermediate'))
        faddress= fake.address()
        femail= fake.email()
        fphonenumber= phonenumbergen()
        hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,address=faddress,email=femail,phonenumber =fphonenumber)
        hydjobs_record = hydjobs_record[0]
        hydjobs_record.save()
populate(25)