from django.urls import path
from myapp.views import * 


urlpatterns = [
    path("",index,name="index"),
    path("categories",categories,name="categories"),
    path("check-out",check_out,name="check_out"),
    path("contact",contact,name="contact"),
    path("main",main,name="main"),
    path("product-page",product_page,name="product_page"),
    path("shopping-cart",shopping_cart,name="shopping_cart"),

]