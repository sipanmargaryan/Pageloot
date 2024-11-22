from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend

from .models import User, Expense
from .schemas import category_summary_schema
from .serializers import UserSerializer, ExpenseSerializer
from .filters import ExpenseFilter


class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ExpenseListCreateView(generics.ListCreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ExpenseFilter

class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer


class ExpenseCategorySummaryView(generics.ListAPIView):
    serializer_class = ExpenseSerializer

    @swagger_auto_schema(manual_parameters=category_summary_schema)
    def get(self, request, *args, **kwargs):
        user_id = request.query_params.get("user")
        month = request.query_params.get("month")

        if not user_id or not month:
            return Response({"error": "user and month parameters are required."}, status=400)

        summary = Expense.get_expense_summary(user_id, month)

        return Response(summary)