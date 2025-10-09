from django.urls import path
from . import views  # Import your views from the current app

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
]