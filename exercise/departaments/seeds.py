import faker
from django.db import transaction
from psycopg2 import IntegrityError

from clients.models import User
from companies.models import Company
from departaments.models import Departament, DepartamentUser, Family


def departament_seed():
    f = faker.Faker()
    departaments = []
    try:
        with transaction.atomic():
            for i in range(700):
                new = Departament()
                new.name = f.company()
                new.company = Company.objects.order_by('?').first()
                new.save()
    except IntegrityError as err:
        last_error = err


def departament_user_seed(seeder):
    seeder.add_entity(DepartamentUser, 80000,{
        'departament': Departament.objects.order_by('?').first(),
        'user': User.objects.order_by('?').first()
    })


def family_seed(seeder):
    seeder.add_entity(Family, 15000, {
        'parent': lambda x: Departament.objects.order_by('?').first(),
        'child': lambda x: Departament.objects.order_by('?').first()
    })


def all_seed(seeder):
    departament_seed()
    departament_user_seed(seeder)
    family_seed(seeder)
    return seeder
