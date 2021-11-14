# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user, logout_view, profile_view
from django.contrib.auth.views import LogoutView

app_name = 'authentication'

urlpatterns = [
    path('register/', register_user, name="register"),
    path('login/', login_view, name="login"),
    path('profile/', profile_view, name="profile"),
    # path('logout/', logout_view, name="logout"),
    path("logout/", LogoutView.as_view(template_name='accounts/logout.html'), name="logout")
]
