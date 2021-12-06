from clients.models import User, AdditionalInfo


def user_seed(seeder):
    """
    Creating User instance
    :params seeder Seeder from django_seed instance
    """
    seeder.add_entity(User, 50000)


def addition_info_seed(seeder):
    """
    Creating Additional info instance for Users
    :params seeder Seeder from django_seed instance
    """
    seeder.add_entity(AdditionalInfo, 50000*3)


def all_seed(seeder):
    """
    Running all companies seeds
    :params seeder Seeder from django_seed instance
    """
    user_seed(seeder)
    addition_info_seed(seeder)
    return seeder
