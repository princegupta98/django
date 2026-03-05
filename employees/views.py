from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from employees.forms import EmployeeForm
from employees.models import Employee


# Create your views here.
def employee_details(request, pk):

    # try:
    # 	employee = Employee.objects.get(pk=pk)
    # 	print(employee)
    # except:
    # 	raise Http404

    # Using django shortcuts
    employee = get_object_or_404(Employee, pk=pk)
    context = {"employee": employee}
    return render(request, "employee_detail.html", context)


def employee_form(request, id=0):
    #
    if request.method == "GET":
        if id == 0:
            form = EmployeeForm()
        else:
            emp = Employee.objects.get(pk=id)
            form = EmployeeForm(instance=emp)

        return render(request, "employee_form.html", {"form": form})

    # POST - update, insert
    else:
        if id == 0:
            form = EmployeeForm(request.POST, request.FILES)
            # print('received in insert operation')
            # print(form.is_valid())
            # print(form.errors)
        else:
            emp = Employee.objects.get(pk=id)
            form = EmployeeForm(request.POST, request.FILES, instance=emp)

        if form.is_valid():
            form.save()
            print("employee saved")
        return redirect("/")  # project's route with employee list


def employee_delete(request,id):
    emp = Employee.objects.get(pk=id)
    emp.delete()
    return redirect("/")
