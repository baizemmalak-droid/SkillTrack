from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('complete/<int:challenge_id>/', views.complete_challenge, name='complete_challenge'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
]








