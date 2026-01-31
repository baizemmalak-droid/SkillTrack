from django.urls import path
from . import views

app_name = 'skill_exchange'

urlpatterns = [
    path('', views.landing_page, name='skill_home'),
    path('my_skills/', views.my_skills, name='my_skills'),
    path('add/', views.add_skill, name='add_skill'),
    path('skill_guidance/', views.skill_guidance, name='skill_guidance'),
]