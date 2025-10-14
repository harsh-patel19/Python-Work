from django.shortcuts import render,HttpResponse
from HARSHAPP.models import *
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.

def index(request):
    return render(request,"index.html")