from django.contrib import admin
from APP.models import *
# Register your models here.

class CategoryModel(admin.ModelAdmin):
    list_display=['id','name','image']

class ProductModel(admin.ModelAdmin):
    list_display=['id','name','peice','qty','image','category']



admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)