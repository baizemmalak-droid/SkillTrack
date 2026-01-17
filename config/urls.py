from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('challenges.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('challenges/', include('challenges.urls')),
]


