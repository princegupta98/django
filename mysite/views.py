from django.http import HttpResponse
from django.shortcuts import render
from employees.models import Employee

def employee_list(request):
    # return HttpResponse("Home Page")

    # return render(request, "home.html")

    employees = Employee.objects.all()
    print(employees)

    context = {
        'employees' : employees
    }

    return render(request, "employee_list.html", context)
