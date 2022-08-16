import random
from django_seed import Seed
from employees.models import EmployeesList


def run():
    """
        Seed DB with employee's details.
        Parametrs:
        Level - numbers of hierarchy levels
        Start - number of records for first level hierarchy.
        Step - increase number of records for every level
    """
    seeder = Seed.seeder()

    def db_seed(level=5, start=5000, step=2500):
        inserted_pks = {}
        i = 0
        while i < level:
            seeder.add_entity(EmployeesList, start, {
                'fullname': lambda x: seeder.faker.name_nonbinary(),
                'position': lambda x: seeder.faker.job(),
                'employment_date': lambda x: seeder.faker.date_between(start_date='-2y'),
                'salary': lambda x: seeder.faker.pydecimal(8, 2, True, 50000, 100000),
                'supervisor_id': lambda x: random.choice(inserted_pks.get(EmployeesList, [None])),
            })
            inserted_pks = seeder.execute()
            start += step
            i += 1
        rows = len(EmployeesList.objects.all())
        print('Totally added:', rows, 'rows')
    db_seed()
