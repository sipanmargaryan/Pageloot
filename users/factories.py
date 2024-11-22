import random
import factory

from django.contrib.auth import get_user_model
from .models import Expense


class UserFactory(factory.django.DjangoModelFactory):
    username = factory.Faker('user_name')
    email = factory.Faker('email')

    class Meta:
        model = get_user_model()


class ExpenseFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Expense

    user = factory.SubFactory(UserFactory)
    title = factory.Faker('sentence', nb_words=3)
    amount = factory.Faker('pydecimal', left_digits=4, right_digits=2, positive=True) 
    date = factory.Faker('date_between', start_date='-1y', end_date='today')
    category = factory.LazyFunction(lambda: random.choice([choice[0] for choice in Expense.CATEGORY_CHOICES]))