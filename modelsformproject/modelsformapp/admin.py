from django.contrib import admin
from modelsformapp.models import Student


class StudentAdmin(admin.ModelAdmin):
    list_display=['name','marks']

admin.site.register(Student,StudentAdmin)
