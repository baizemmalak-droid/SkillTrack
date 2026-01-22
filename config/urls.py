from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('user_auth_home.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('profile/', include('profile_app.urls')),  
    path('challenges/', include('skilltrack_challenges.urls')),
    path('skills/', include('skill_exchange.urls')),

]


