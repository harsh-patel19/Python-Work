from django.shortcuts import render,HttpResponse

# Create your views here.

def index(request):
    # return HttpResponse("Home")
    return render(request,'index.html')

def about(request):
    # return HttpResponse("About")
    return render(request,'about.html')

def contact(request):
    # return HttpResponse("contact us")
    return render(request,'contact.html')