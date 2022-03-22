from http.client import HTTPResponse
from django.shortcuts import render

from .models import Employee

# Create your views here.

def employee_data(request):

    employees = Employee.objects.all()

    for employee in employees:
        print(employee.name,employee.company.name)
    
