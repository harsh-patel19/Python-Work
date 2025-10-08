from django.contrib import admin
from myapp.models import *

# Register your models here.

class categoryModel(admin.ModelAdmin):
    list_display=['id','name','image']


class ProductModel(admin.ModelAdmin):
    list_display=['id','name','price','qty','image','category']


admin.site.register(Category,categoryModel)
admin.site.register(Product,ProductModel)