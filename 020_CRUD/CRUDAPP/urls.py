from django.urls import path
from CRUDAPP.views import *

urlpatterns = [

    path("",index,name="index"),
]