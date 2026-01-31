from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from collections import defaultdict

from .models import Challenge, ChallengeSubmission, UserBadge

# ---------- HELPERS ----------
def is_unlocked(user, challenge):
    if challenge.level == "easy":
        return True

    if challenge.level == "intermediate":
        return ChallengeSubmission.objects.filter(
            user=user,
            challenge__skill=challenge.skill,
            challenge__level="easy",
            is_approved=True
        ).exists()

    if challenge.level == "advanced":
        return ChallengeSubmission.objects.filter(
            user=user,
            challenge__skill=challenge.skill,
            challenge__level="intermediate",
            is_approved=True
        ).exists()

    return False


# ---------- CHALLENGES LIST ----------
@login_required
def challenges_list(request):
    challenges = Challenge.objects.all().order_by("skill__name", "level")
    grouped = defaultdict(list)

    for c in challenges:
        c.unlocked = is_unlocked(request.user, c)

        submission = ChallengeSubmission.objects.filter(
            user=request.user,
            challenge=c
        ).first()

        c.submission = submission
        grouped[c.skill.name].append(c)

    return render(request, "skilltrack_challenges/challenges_list.html", {
        "grouped_challenges": dict(grouped)
    })


# ---------- CHALLENGE DETAIL ----------
@login_required
def challenge_detail(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)

    submission = ChallengeSubmission.objects.filter(
        user=request.user,
        challenge=challenge
    ).first()

    unlocked = is_unlocked(request.user, challenge)

    return render(request, "skilltrack_challenges/challenge_detail.html", {
        "challenge": challenge,
        "submission": submission,
        "unlocked": unlocked,
    })

# ---------- SUBMIT ----------
@login_required
def submit_challenge(request, challenge_id):
    challenge = get_object_or_404(Challenge, id=challenge_id)

    submission = ChallengeSubmission.objects.filter(
        user=request.user,
        challenge=challenge
    ).first()

    if request.method == "POST":
        solution = request.POST.get("solution", "").strip()

        from .validators import validate_solution
        passed = validate_solution(challenge, solution)

        if submission:
            # 🔁 UPDATE (Try again)
            submission.solution = solution
            submission.is_approved = passed
            submission.save()
        else:
            # 🆕 FIRST SUBMISSION
            ChallengeSubmission.objects.create(
                user=request.user,
                challenge=challenge,
                solution=solution,
                is_approved=passed
            )

    return redirect(
        "skilltrack_challenges:challenge_detail",
        challenge_id=challenge.id
    )


# ---------- LEADERBOARD ----------
@login_required
def leaderboard(request):
    users = User.objects.all().order_by("-userprofile__points")
    return render(request, "skilltrack_challenges/leaderboard.html", {
        "users": users
    })


# ---------- BADGES ----------
@login_required
def my_badges(request):
    badges = UserBadge.objects.filter(user=request.user)
    return render(request, "skilltrack_challenges/my_badges.html", {
        "badges": badges
    })
