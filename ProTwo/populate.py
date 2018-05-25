import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

import random
from AppTwo.models import user
from faker import Faker

fakegen = Faker()

def Populate(n=5):
    for a in range(n):
        fake_name = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.free_email()

        fill = user.objects.get_or_create(first_name=fake_name,last_name=fake_lname,email=fake_email)[0]

if __name__ == '__main__':
    print("Populate")
    Populate(20)
    print("Done")
