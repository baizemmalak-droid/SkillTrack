from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile_view(request):
    context = {
        "user": request.user,
        "skills": [],
        "challenges": [],
    }
    return render(request, "profile/profile.html", context)