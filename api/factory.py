import factory
from factory.django import DjangoModelFactory
from faker import Faker
from api.models import Category, Product

fake = Faker()

class CategoryFactory(DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.LazyAttribute(lambda x: fake.word().title())
    image_url = factory.LazyAttribute(lambda x: fake.image_url())

class ProductFactory(DjangoModelFactory):
    class Meta:
        model = Product

    name = factory.LazyAttribute(lambda x: fake.word())
    description = factory.LazyAttribute(lambda x: fake.text())
    price = factory.LazyAttribute(lambda x: round(fake.pydecimal(left_digits=3, right_digits=2, positive=True), 2))
    category = factory.SubFactory(CategoryFactory)
    image_url = factory.LazyAttribute(lambda x: fake.image_url())
    featured = factory.LazyAttribute(lambda x: fake.boolean(chance_of_getting_true=30))
