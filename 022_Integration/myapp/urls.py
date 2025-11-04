from django.urls import path
from myapp.views import *

urlpatterns = [
    path('',index,name="index.html"),
    path('payment',payment,name="payment"),
    path('sms',sms,name="sms"),
    path('email',send_email,name="email"),

]