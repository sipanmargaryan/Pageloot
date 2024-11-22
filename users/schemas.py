from drf_yasg import openapi

category_summary_schema = [
    openapi.Parameter(
        name="user",
        in_=openapi.IN_QUERY,
        description="User ID to filter expenses",
        type=openapi.TYPE_INTEGER,
        required=True,
    ),
    openapi.Parameter(
        name="month",
        in_=openapi.IN_QUERY,
        description="Month of the year",
        type=openapi.TYPE_INTEGER,
        required=True,
    ),
]