from django.urls import path
from . import views

app_name = "skilltrack_challenges"

urlpatterns = [
    path('', views.challenges_list, name='challenges_list'),
    path('<int:challenge_id>/', views.challenge_detail, name='challenge_detail'),
    path('submit/<int:challenge_id>/', views.submit_challenge, name='submit_challenge'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('badges/', views.my_badges, name='my_badges'),

]


   

