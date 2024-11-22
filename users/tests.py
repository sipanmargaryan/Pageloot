import pytest
from datetime import datetime

from django.urls import reverse

from .factories import UserFactory, ExpenseFactory

@pytest.mark.django_db
def test_category_summary(client):
    user = UserFactory()
    food_amounts = [10, 20, 30, 40]
    category = "Food"
    
    current_date = datetime.today().date()

    for amount in food_amounts:
        ExpenseFactory(user=user, amount=amount, category=category, date=current_date)

    params = {
        "user": user.id,
        "month": 11,
    }
    response = client.get(reverse('users:expense-category-summary'), params)

    assert response.status_code == 200

    response_data = response.json()
    assert response_data[0]["total"] == sum(food_amounts)
