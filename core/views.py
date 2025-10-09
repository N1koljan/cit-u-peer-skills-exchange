# in core/views.py

from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CustomSignUpForm


def signup_view(request):
    if request.method == 'POST':
        print("✅ POST request received!")

        form = CustomSignUpForm(request.POST)

        print("Is the form valid?", form.is_valid())
        print("Form Errors:", form.errors.as_json())

        if form.is_valid():
            user = form.save()
            messages.success(request, f'Account for {user.username} created successfully! You can now log in.')
            return redirect('login')
    else:
        form = CustomSignUpForm()

    return render(request, 'ui/signup.html', {'form': form})