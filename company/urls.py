from django.urls import path

from .views import employee_data

urlpatterns = [
    path('',employee_data, name = "employee")
]
