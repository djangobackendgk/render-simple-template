from django.contrib import admin
from .models import *
# Register your models here.

class teacherAdmin(admin.ModelAdmin):
	list_display=["firstName","lastName","fullName"]

admin.site.register(teacher,teacherAdmin)
