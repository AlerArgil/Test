from clients.models import User, AdditionalInfo


def user_seed(seeder):
    seeder.add_entity(User, 50000)


def addition_info_seed(seeder):
    seeder.add_entity(AdditionalInfo, 50000*5)


def all_seed(seeder):
    user_seed(seeder)
    addition_info_seed(seeder)
    return seeder
