from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"index.html")

def categories(request):
    return render(request,"categories.html")

def check_out(request):
    return render(request,"check_out.html")

def contact(request):
    return render(request,"contact.html")

def main(request):
    return render(request,"main.html")

def product_page(request):
    return render(request,"product_page.html")

def shopping_cart(request):
    return render(request,"shopping_cart.html")
