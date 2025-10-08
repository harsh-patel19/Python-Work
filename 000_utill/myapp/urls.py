from django.urls import path
from myapp.views import *
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',index,name='index'),
    path('accounts',accounts,name='accounts'),
    path('base',base,name='base'),
    path('cart',cart,name='cart'),
    path('checkout',checkout,name='checkout'),
    path('compare',compare,name='compare'),
    path('detail',detail,name='detail'),
    path('loginregister',loginregister,name='loginregister'),
    path('shop',shop,name='shop'),
    path('wishlist',wishlist,name='wishlist'),


]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)