
from django.contrib import admin
from Myapp.models import *
# Register your models here.

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Address)
admin.site.register(UserOrder)
admin.site.register(OrderDetails)