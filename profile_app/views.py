from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import UserPresentation
from skilltrack_challenges.models import ChallengeSubmission, UserBadge
from skill_exchange.models import UserSkill


@login_required
def profile_view(request):
    user = request.user

    # Get or create presentation object
    presentation_obj, created = UserPresentation.objects.get_or_create(user=user)

    # HANDLE FORM SUBMISSION
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        education = request.POST.get("education")
        level = request.POST.get("level")
        goal = request.POST.get("goal")

        # If professional questions are filled
        if full_name and education and level and goal:
            presentation_text = (
                f"My name is {full_name}. "
                f"I am currently a {level} studying {education}. "
                f"My professional objective is {goal}. "
                f"I am motivated to continuously develop my skills through SkillTrack."
            )
            presentation_obj.presentation = presentation_text
        else:
            # Fallback: manual presentation text
            presentation_obj.presentation = request.POST.get("presentation")

        presentation_obj.save()

    # 1️⃣ Challenges completed by the user
    submissions = ChallengeSubmission.objects.filter(user=user)
    challenges = [s.challenge for s in submissions]

    # 2️⃣ User skills
    skills = UserSkill.objects.filter(user=user).select_related("skill")

    # 3️⃣ User badges
    user_badges = UserBadge.objects.filter(user=user)
    badges = [ub.badge for ub in user_badges]

    context = {
        "user": user,
        "presentation": presentation_obj.presentation,
        "challenges": challenges,
        "skills": skills,
        "badges": badges,
    }

    return render(request, "profile/profile.html", context)
