from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import  Task

# Register your models here.
admin.site.register(Task)