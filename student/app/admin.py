from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Studdata)
class StuddataModelAdmin(admin.ModelAdmin):
    list_display = ['name','clas','rollno','FEcgpa','Hobbies','Reviews']