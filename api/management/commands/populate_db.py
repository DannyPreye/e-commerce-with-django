from django.core.management.base import BaseCommand
from faker import Faker


from api.models import Category, Product
from api.factory import CategoryFactory, ProductFactory

class Command(BaseCommand):
    help = 'Populate the database with sample data'

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Create 5 categories
        categories = [CategoryFactory() for _ in range(5)]

        # Create 20 products
        products = [ProductFactory(category=fake.random.choice(categories)) for _ in range(20)]

        self.stdout.write(self.style.SUCCESS('Database populated with sample data'))
