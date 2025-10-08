from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from myapp.models import *
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    Categories = Category.objects.all()
    Products = Product.objects.all()
    try:
        cid = int(request.GET['cid'])

        if cid!=0:
            Product = Product.objects.filter(Category_id=cid)
        else:
            Products= Product.obeject.all()
        return render(request,"index.html",{"categories":Categories,"products":Products})
    except Exception as e:
        return render(request,'index.html')

@login_required(login_url="loginregister")
def accounts(request):
    return render(request,'accounts.html')

@login_required(login_url="loginregister")
def base(request):
    return render(request,'base.html')

@login_required(login_url="loginregister")
def cart(request):
    return render(request,'cart.html')

@login_required(login_url="loginregister")
def checkout(request):
    return render(request,'checkout.html')

def compare(request):
    return render(request,'compare.html')

def detail(request):
    return render(request,'detail.html')

def loginregister(request):
    return render(request,'loginregister.html')

def wishlist(request):
    return render(request,'wishlist.html')

def shop(request):
    return render(request,'shop.html')

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        user = User.objects.filter(username=username).exists()
        if user:
            return render(request,"loginregister.html",{"rerr":"username alredy exits"})
        u = user(username=username,email=email)
        u.set_password(password)
        u.save()
        return render(request,"loginregister.html",{"msg":"user registerd successfully"})
    return render(request,'register.html')


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username,password=password)
        if user:
            login(request,user)
            return render(request,"index.html")
        else:
            return render(request,"loginregister.html",{"err":"Invalid username or password"})
    return render(request,"loginregister.html")


def user_logout(request):
    logout(request)
    return redirect("index")