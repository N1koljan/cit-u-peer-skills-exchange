from django.shortcuts import render

def home(request):
    return render(request, 'ui/index.html')
def login_view(request):
    return render(request, 'ui/auth/login.html')
def signup_view(request):
    return render(request, 'ui/auth/signup.html')
def dashboard_view(request):
    return render(request, 'ui/student/dashboard.html')
def profile_view(request):
    return render(request, 'ui/student/profile.html')
def edit_profile_view(request):
    return render(request, 'ui/student/edit_profile.html')
def my_skill_view(request):
    return render(request, 'ui/student/my_skills.html')
def request_view(request):
    return render(request, 'ui/student/request.html')
def find_skill_view(request):
    return render(request, 'ui/student/find_skills.html')
def session_view(request):
    return render(request, 'ui/student/session.html')
def skill_view(request):
    return render(request, 'ui/student/skill.html')