
from django.urls import path
from HARSHAPP.views import *


urlpatterns =[
    path("",index, name="index"),
    path("register",register,name="register"),
    path("display",display,name="display"),
    path("load",load,"load")

]