from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True)

    
    def __str__(self):
        return f'{self.username}'
    

class Expense(models.Model):
    CATEGORY_CHOICES = [
        ('Food', 'Food'),
        ('Travel', 'Travel'),
        ('Utilities', 'Utilities'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    title = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    
    def __str__(self):
        return f"{self.title} - {self.user.username}"
    
    @classmethod
    def get_expense_summary(cls, user_id, month):
        expenses = Expense.objects.filter(user_id=user_id, date__month=month)
        return expenses.values('category').annotate(total=models.Sum('amount'))