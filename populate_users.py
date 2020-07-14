import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_two.settings')

import django
django.setup()

from app_two.models import User
from faker import Faker

faker_generator = Faker()

def generate_user():
  fake_first_name = faker_generator.first_name()
  fake_last_name = faker_generator.last_name()
  fake_email = faker_generator.email()
  user = User.objects.get_or_create(first_name= fake_first_name, last_name=fake_last_name, email= fake_email)[0]
  user.save()
  return user

def seed(total=5):
  for record in range(total):
    user = generate_user()

    print('User: ' + str(user))

if __name__ == '__main__':
  print('Populating script!')
  seed(10)
  print('Populating compleate!')
