from django.shortcuts import render

# Create your views here.
# ui/views.py

from django.shortcuts import render

def index(request):
    """
    This view renders the homepage (index.html).
    """
    return render(request, 'ui/index.html')

def login_view(request):
    """
    This view renders the login page (login.html).
    """
    # For now, we are just displaying the page.
    # Later, you will add logic here to handle the form submission.
    return render(request, 'ui/login.html')

def signup_view(request):
    """
    This view will render the signup page. We are creating it as a placeholder
    so the link on your login page doesn't cause an error.
    """
    # You would create a signup.html and render it here.
    # For now, we can just return the login page again as a temporary measure.
    return render(request, 'ui/login.html') # Placeholder