# In ui/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from core.forms import CustomSignUpForm
from core.forms import CustomLoginForm, CustomSignUpForm
from django.contrib.auth import login


def home(request):
    return render(request, 'ui/index.html')


def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')

    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect('profile')
    else:
        form = CustomLoginForm()

    return render(request, 'ui/auth/login.html', {'form': form})


def signup_view(request):
    if request.method == 'POST':

        print("✅ POST request received in ui/views.py!")
        form = CustomSignUpForm(request.POST)
        print("Is the form valid?", form.is_valid())
        print("Form Errors:", form.errors.as_json())
        # ----------------------------

        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account for {user.username} created successfully! You can now log in.')
            return redirect('login')
    else:
        form = CustomSignUpForm()

    return render(request, 'ui/auth/signup.html', {'form': form})

def profile_view(request):
    return render(request, 'ui/profile.html', {'user': request.user})
# --------------------------------