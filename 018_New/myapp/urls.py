
from django.urls import path
from myapp.views import *


urlpatterns =[
    path('',index,name='index'),
    path('cart',cart,name='cart'),
    path('chackout',chackout,name='chackout'),
    path('contact',contact,name='contact'),
    path('shop_detail',shop_detail,name='shop_detail'),
    path('shop',shop,name='shop'),
]