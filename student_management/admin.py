from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import College, Student

admin.site.register(College)
admin.site.register(Student)