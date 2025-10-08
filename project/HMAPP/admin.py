from django.contrib import admin
from HMAPP.models import *
# Register your models here.

class CategoryModel(admin.ModelAdmin):
    list_display=['id','name','image']

class ProductModel(admin.ModelAdmin):
    list_display=['id','name','price','qty','image','Category','description']



admin.site.register(Category,CategoryModel)
admin.site.register(Product,ProductModel)