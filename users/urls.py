from django.urls import path


from .views import (
    UserListCreateView,
    ExpenseListCreateView,
    ExpenseDetailView,
    ExpenseCategorySummaryView,
)

app_name = 'users'

urlpatterns = [
    path('users/', UserListCreateView.as_view(), name='user-list-create'),
    path('expenses/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expenses/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
    path('expenses/category-summary/', ExpenseCategorySummaryView.as_view(), name='expense-category-summary'),
]