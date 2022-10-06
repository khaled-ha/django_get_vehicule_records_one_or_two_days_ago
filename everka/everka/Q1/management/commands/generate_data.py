from django.core.management.base import BaseCommand, CommandError
from django_seed import Seed
from Q1.models import Vehicule, NavigationRecord
from datetime import date
import datetime
class Command(BaseCommand):
    help = 'this command to generate fake data'

    def handle(self, *args, **options):
        today = date.today()
        year = today.year
        month = today.month
        day = today.day
        seeder = Seed.seeder()
        seeder.add_entity(Vehicule, 15)
        seeder.add_entity(NavigationRecord,15,{'datetime':    lambda x:datetime.date(year, month, day-1)})
        seeder.add_entity(NavigationRecord,15,{'datetime':    lambda x:datetime.date(year, month, day)})
        seeder.execute()




