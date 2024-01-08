import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysqlsampleproject.settings')

# Ensure that Django is set up before importing models
django.setup()

from mysqlsampleapp.models import *
from faker import Faker
from random import randint

fake = Faker()

def phonenumbergen():
    d1 = randint(7, 9)
    num = '' + str(d1)
    for i in range(8):
        num = num + str(randint(0, 9))
    return num

def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.job()
        feligibility = fake.random_element(elements=('Fresher', 'Experienced', 'Intermediate'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        
        hydjobs_record = hydjobs.objects.get_or_create(
            date=fdate,
            company=fcompany,
            title=ftitle,
            eligibility=feligibility,
            address=faddress,
            email=femail,
            phonenumber=fphonenumber
        )[0]
        hydjobs_record.save()

# Call the populate function with the desired number of entries
populate(25)
