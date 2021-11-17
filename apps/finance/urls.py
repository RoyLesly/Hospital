from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from .views import welcome_view

app_name = 'finance'

urlpatterns = [
    path('', welcome_view, name="welcome"),
]
