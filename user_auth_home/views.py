from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password
from datetime import timedelta
from django.utils import timezone

def login_view(request):
    # Vider les anciens messages
    storage = messages.get_messages(request)
    storage.used = True

    # Redirection si déjà connecté
    if request.user.is_authenticated:
        return redirect('dashboard')

    FAILED_ATTEMPTS_KEY = 'failed_attempts'
    LOCK_UNTIL_KEY = 'lock_until'

    # Initialiser le compteur si inexistant
    if FAILED_ATTEMPTS_KEY not in request.session:
        request.session[FAILED_ATTEMPTS_KEY] = 0

    # Vérifier si l'utilisateur est temporairement bloqué
    if LOCK_UNTIL_KEY in request.session:
        lock_until = request.session[LOCK_UNTIL_KEY]
        if timezone.now() < timezone.datetime.fromisoformat(lock_until):
            remaining = timezone.datetime.fromisoformat(lock_until) - timezone.now()
            minutes = int(remaining.total_seconds() // 60) + 1
            messages.error(
                request,
                f"Too many failed login attempts. Please try again in {minutes} minutes."
            )
            return render(request, 'user_auth_home/login.html')
        else:
            # Débloquer l'utilisateur
            del request.session[LOCK_UNTIL_KEY]
            request.session[FAILED_ATTEMPTS_KEY] = 0

    # Si formulaire soumis
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Reset compteur et blocage
            request.session[FAILED_ATTEMPTS_KEY] = 0
            request.session.pop(LOCK_UNTIL_KEY, None)

            # Connexion
            login(request, user)
            return redirect('dashboard')

        else:
            # Compter l'échec
            request.session[FAILED_ATTEMPTS_KEY] += 1

            # Bloquer après 5 échecs
            if request.session[FAILED_ATTEMPTS_KEY] >= 5:
                lock_until = timezone.now() + timedelta(minutes=10)
                request.session[LOCK_UNTIL_KEY] = lock_until.isoformat()

                messages.error(
                    request,
                    "Too many failed login attempts. Your access has been temporarily blocked for 10 minutes."
                )
            else:
                messages.error(request, "Invalid username or password.")

    return render(request, 'user_auth_home/login.html')


def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('register')

      
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
            return redirect('register')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('register')

        temp_user = User(username=username, email=email)

        try:
            validate_password(password1, user=temp_user)
        except ValidationError as e:
            for error in e.messages:
                messages.error(request, error)  
            return redirect('register')

        User.objects.create_user(
            username=username,
            email=email,
            password=password1
        )

        messages.success(request, "Account created successfully. You can now log in.")
        return redirect('login')

    return render(request, 'user_auth_home/register.html')

@login_required
def logout_view(request):
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, 'user_auth_home/home.html')
