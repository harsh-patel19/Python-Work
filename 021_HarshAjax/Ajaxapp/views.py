from django.shortcuts import render,HttpResponse
from Ajaxapp.models import *
from django.http import JsonResponse
# Create your views here.

def index(request):
    return render(request,"index.html")


def search(reuqest):
    data = reuqest.GET['data']
    products = Product.objects.filter(name=data)

    # print(data)
    # return HttpResponse("done")

    return JsonResponse({"data":list(products.values())})

