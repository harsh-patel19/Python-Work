from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def blogdetail(request):
    return render(request,'blog-detail.html')

def blog(request):
    return render(request,'blog.html')

def contact(request):
    return render(request,'contact.html')

def home02(request):
    return render(request,'home02.html')

def home03(request):
    return render(request,'home03.html')

def productdeatil(request):
    return render(request,'productdeatil.html')

def product(request):
    return render(request,'product.html')


def shopingcart(request):
    return render(request,'shopingcart.html')

def login(request):
    return render(request,'login.html')


def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.filter(username=username).exists()
        if user:
            return render(request,"login.html",{"rerr":"Username Already Exists"})
        u = User(username=username,email=email)
        u.set_password(password)
        u.save()
        return render(request,"login.html",{"msg":"User Registered Successfully"})
    return render(request,"login.html")

def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return render(request,"index.html")
        else:
            return render(request,"login-register.html",{"err":"Invalid Username or Password"})
            
    return render(request,"login-register.html")