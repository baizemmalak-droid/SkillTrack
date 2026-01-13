from django.shortcuts import render

def skills_home(request):
    return render(request, 'skills_home.html')

def request_skill(request):
    return render(request, 'request.html')