from django.shortcuts import render
from .models import Challenge

def home(request):
    return render(request, 'challenges/home.html')


def challenge_list(request):
    challenges = Challenge.objects.all()
    return render(request, 'challenges/challenge_list.html', {
        'challenges': challenges
    })








