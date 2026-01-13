from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SkillRequest

def skills_home(request):
    return render(request, 'skills_home.html')


@login_required
def request_skill(request):
    if request.method == 'POST':
        skill_name = request.POST.get('skill_name')
        description = request.POST.get('description')

        SkillRequest.objects.create(
            user=request.user,
            skill_name=skill_name,
            description=description
        )

        return redirect('skills_home')

    return render(request, 'request.html')