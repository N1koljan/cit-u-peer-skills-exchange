from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('edit_profile/', views.edit_profile_view, name='edit_profile'),
    path('my_skill/', views.my_skill_view, name='my_skill'),
    path('request/', views.request_view, name='request'),
    path('find_skill/', views.find_skill_view, name='request'),
    path('session/', views.session_view, name='session'),
    path('skill/', views.skill_view, name='skill'),
    path('logout/', views.logout_view, name='logout'),
]
