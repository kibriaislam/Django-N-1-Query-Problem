from http.client import HTTPResponse
from django.shortcuts import render

from .models import Employee

# Create your views here.

def employee_data(request):
    #employees = Employee.objects.all().select_related("company")
    employees = Employee.objects.all().prefetch_related("company")

    for employee in employees:
        print(employee.name,employee.company.name)
    
    data = {
        'employees':employees
    }
    return render(request,'index.html', data)
    
