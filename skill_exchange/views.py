from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Skill, UserSkill


@login_required
def landing_page(request):
    return render(request, 'skill_exchange/landing_page.html')


@login_required
def my_skills(request):
    user_skills = UserSkill.objects.filter(user=request.user).select_related('skill')
    return render(request, 'skill_exchange/my_skills.html', {
        'user_skills': user_skills
    })


@login_required
def add_skill(request):
    if request.method == 'POST':
        skill_id = request.POST.get('skill')
        level = request.POST.get('level')

        if not skill_id or not level:
            messages.error(request, "Please select a skill and level.")
            return redirect('add_skill')

        try:
            skill = Skill.objects.get(id=skill_id)
            UserSkill.objects.update_or_create(
                user=request.user,
                skill=skill,
                defaults={'level': level}
            )
            messages.success(request, "Skill saved successfully.")
            return redirect('my_skills')

        except Skill.DoesNotExist:
            messages.error(request, "Skill not found.")
            return redirect('add_skill')

    skills = Skill.objects.all().order_by('name')
    return render(request, 'skill_exchange/add_skill.html', {'skills': skills})