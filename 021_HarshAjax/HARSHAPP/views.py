from django.shortcuts import render,HttpResponse
from HARSHAPP.models import *
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,"index.html")

def register(request):
    if request.method=='POST':
        data = request.POST
        name = data.get('name')
        email = data.get('email')
        phone = data.get('phone')
        age = data.get('age')

        Student.objects.create(name=name,email=email,phone=phone,age=age)
        return HttpResponse("Registration successfull Done !!! ")

def display(request):
    allStudents = Student.objects.all()
    return JsonResponse({"data":list(allStudents.value())})

def load(request):
    pass