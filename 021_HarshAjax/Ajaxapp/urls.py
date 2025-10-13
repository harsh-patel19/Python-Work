
from django.urls import path
from Ajaxapp.views import * 

urlpatterns = [
    path("",index,name="index"),
    path("search",search,name="search")
]