from django.shortcuts import render

def home(request):
    return render(request, 'ui/index.html')
def login_view(request):
    return render(request, 'ui/auth/login.html')
def signup_view(request):
    return render(request, 'ui/auth/signup.html')


# Create your views here.
