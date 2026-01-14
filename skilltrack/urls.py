from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('students.urls')),   # profile / dashboard
    path('', include('accounts.urls')),   # login / register / home
]