from django.contrib import admin
from . import models
# Register your models here.
class movielistadmin(admin.ModelAdmin):
    list_display = ['movie','hero','heroine','releasedate']

admin.site.register(models.movielist,movielistadmin)

