from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import Sum
from .models import Challenge, UserChallenge
from .utils import get_total_points, get_level, award_badges


@login_required
def dashboard(request):
    challenges = Challenge.objects.all()
    user_challenges = UserChallenge.objects.filter(user=request.user, completed=True)
    total_points = get_total_points(request.user)
    level = get_level(total_points)

    return render(request, 'challenges/dashboard.html', {
        'challenges': challenges,
        'total_points': total_points,
        'completed_count': user_challenges.count(),
        'level': level
    })


@login_required
def complete_challenge(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)
    uc, created = UserChallenge.objects.get_or_create(
        user=request.user,
        challenge=challenge
    )

    if not uc.completed:
        uc.completed = True
        uc.completed_at = timezone.now()
        uc.save()
        award_badges(request.user)

    return redirect('dashboard')


def leaderboard(request):
    users = []
    for uc in UserChallenge.objects.filter(completed=True):
        if uc.user not in users:
            users.append(uc.user)

    ranking = []
    for user in users:
        ranking.append({
            'user': user,
            'points': get_total_points(user),
            'level': get_level(get_total_points(user))
        })

    ranking.sort(key=lambda x: x['points'], reverse=True)

    return render(request, 'challenges/leaderboard.html', {
        'ranking': ranking
    })
