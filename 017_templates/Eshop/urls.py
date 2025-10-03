from django.urls import path
from Eshop.views import *

urlpatterns=[

    path('',index,name='index'),
    path('about',about,name='about'),
    path('blogdetail',blog_detail,name='blog-detail'),
    path('blog',blog,name='blog'),
    path('contact',contact,name='contact'),
    path('home02',home_02,name='home-02'),
    path('home03',home_03,name='home-03'),
    path('productdetail',product_detail,name='product-detail'),
    path('product',product,name='product'),
    path('shopingcart',shoping_cart,name='shoping-cart')

]