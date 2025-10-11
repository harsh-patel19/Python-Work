from django.shortcuts import render
from emp_app.models import Employee,Role,Department
# Create your views here.

def index(request):
    return render(request,'index.html')

def all_emp(request):
    return render(request,'view_all_emp.html')

def add_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps': emps
    }
    print(context)
    return render(request,'add_emp.html',context)

def remove_emp(request):
    return render(request,'remove_emp.html')

def filter_emp(request):
    return render(request,'filter_emp.html')