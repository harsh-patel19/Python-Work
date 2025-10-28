from django.urls import path
from HMAPP.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("",index,name="index"),
    path("about",about,name="about"),
    path("blogdetail",blogdetail,name="blogdetail"),
    path("blog",blog,name="blog"),
    path("contact",contact,name="contact"),
    path("home02",home02,name="home02"),
    path("home03",home03,name="home03"),
    path("productdeatil",productdeatil,name="productdeatil"),
    path("product",product,name="product"),
    path("shopingcart",shopingcart,name="shopingcart"),
    path("login",login,name="login"),
    path("register",register,name="register"),
    path("user-logout",user_logout,name="user-logout"),

    path("addtocart",add_to_cart,name="addtocart"),

    path("allcategories",allcategories,name="allcategories")
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)