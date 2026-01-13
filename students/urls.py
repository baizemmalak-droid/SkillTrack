from django.urls import path
from . import views

urlpatterns = [
    path('profile/', views.profile_view, name='profile'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/edit/', views.edit_profile, name='edit_profile'),
]
from django.http import HttpResponse

def test(request):
    return HttpResponse("PROJECT URLS WORK")
    path('test/', test),