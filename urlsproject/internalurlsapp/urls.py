from django.contrib import admin
from django.urls import path
from internalurlsapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hydjobs/', admin.site.urls),
    path('chennaijobs/', admin.site.urls),
    path('mumbaijobs/', admin.site.urls),
    path('bangalorejobs/', admin.site.urls),
]
