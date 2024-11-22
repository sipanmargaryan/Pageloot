from django_filters import rest_framework as filters
from .models import Expense

class ExpenseFilter(filters.FilterSet):
    start_date = filters.DateFilter(field_name="date", lookup_expr="gte", label="Start Date")
    end_date = filters.DateFilter(field_name="date", lookup_expr="lte", label="End Date")
    category = filters.CharFilter(field_name="category", lookup_expr="iexact", label="Category")

    class Meta:
        model = Expense
        fields = ['start_date', 'end_date', 'category']