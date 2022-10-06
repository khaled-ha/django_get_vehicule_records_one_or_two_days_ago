from django.urls import path, include
from .views import get_records

urlpatterns = [
    path('', get_records, name="records"),
]
