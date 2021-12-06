from random import randint

from companies.models import Company


def company_seed(seeder):
    """
    Creating Company instance
    :params seeder Seeder from django_seed instance
    """
    seeder.add_entity(Company, 300, {
        'inn': lambda x: str(randint(100000000000, 999999999999)),
        'kpp': lambda x: str(randint(100000000, 999999999))
    })


def all_seed(seeder):
    """
    Running all companies seeds
    :params seeder Seeder from django_seed instance
    """
    company_seed(seeder)
    return seeder
