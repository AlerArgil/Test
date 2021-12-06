from django_seed import Seed

import departaments.seeds, clients.seeds, companies.seeds

from django.core.management import BaseCommand


class Command(BaseCommand):
    help = 'seeds models'

    def handle(self, *args, **options):
        seeder = Seed.seeder()
        print('clients seed start')
        clients.seeds.all_seed(seeder)
        print('clients seed end\ncompanies seed start')
        companies.seeds.all_seed(seeder)
        print('companies seed end\n departaments seed start')
        departaments.seeds.all_seed(seeder)
        print('departaments seed end')
        seeder.execute()
        print('Seeds complete')
