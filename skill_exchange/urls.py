from django.urls import path
from . import views

urlpatterns = [
    path('', views.skills_home, name='skills_home'),
    path('request/', views.request_skill, name='request_skill'),
]