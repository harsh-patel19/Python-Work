from django.urls import path 
from crudapp.views import *

urlpatterns = [
    path("get",get_data,name="get"),
    path("add",add_data,name="add"),
]