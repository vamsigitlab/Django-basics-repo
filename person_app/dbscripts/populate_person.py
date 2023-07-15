'''
python manage.py shell
execute the below command inside the shell
exec(open('./person_app/dbscripts/populate_person.py').read())

open a file 
read a file 
execute a file

'''
from faker import Faker
from person_app.models import Person
AGE = [i for i in range(1,99)]
MAX_LIMIT = 1000
fake = Faker()
class PopulatePerson():
    def __init__(self) -> None:
        pass
    def fetch_age(self):
        return fake.random_choices(elements=AGE, length=1)
    
    def run(self):
        for i in range(0,MAX_LIMIT):
            name = fake.name()
            age = self.fetch_age()[0] 
            Person.objects.create(
                name = name,
                age = age,
            )

populate_person = PopulatePerson()
populate_person.run()
