# !!! FOR DEVELOPERS ONLY ( MAKES DUMMY DATA FOR THE DICTIONARY TABLE VIEW )  !!!
# !!! FOR DEVELOPERS ONLY ( MAKES DUMMY DATA FOR THE DICTIONARY TABLE VIEW )  !!!
# !!! FOR DEVELOPERS ONLY ( MAKES DUMMY DATA FOR THE DICTIONARY TABLE VIEW )  !!!
# !!! IF YOU WANT TO RUN THIS SCRIPT USE COMMAND python manage.py generate_dummy_data  !!!
import random
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from faker import Faker

from vocab.models import Word, Category

fake_en = Faker('en-US')
fake_ua = Faker("uk_UA")


class Command(BaseCommand):
    help = 'Generate dummy data for your database tables'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Generating dummy data...'))
        status = [i for i in range(0, 101, 10)]
        categories = Category.objects.all()

        for _ in range(5):  # Adjust the number of records as needed
            Word.objects.create(
                en_word=fake_en.word()[0:19],
                ua_word=fake_ua.color_name()[0:19],
                category=random.choice(categories),
                owner=User.objects.get(username='test'),  # Replace with logic to get a valid user
                status=random.choice(status),
            )

        self.stdout.write(self.style.SUCCESS('Dummy data generated successfully.'))
