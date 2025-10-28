from django.contrib import admin
from HARSHAPP.models import *

# Register your models here.
class Studentmodel(admin.ModelAdmin):
    list_display=['id','name','email','phone','age']



admin.site.register(Student,Studentmodel)

