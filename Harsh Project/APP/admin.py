from django.contrib import admin
from APP.models import *
# Register your models here.

class CategoryModel(admin.ModelAdmin):
    list_display=['id','name','image']

class ProductModel(admin.ModelAdmin):
    list_display=['id','name','price','qty','image','category']



admin.site.register(Category,CategoryModel)
admin.site.register(Product,ProductModel)
admin.site.register(Cart)