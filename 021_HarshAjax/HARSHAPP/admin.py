from django.contrib import admin
from HARSHAPP.models import *

# Register your models here.
class Studentmodel(admin.ModelAdmin):
    list_display=['id','name','email','phone','age']

class DepartmentModel(admin.ModelAdmin):
    list_display=['id','name']





admin.site.register(Student,Studentmodel)
admin.site.register(Department,DepartmentModel)