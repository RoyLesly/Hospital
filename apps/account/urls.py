# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView
from apps.account.views import profile_view

app_name = 'account'

urlpatterns = [
    path('profile/', profile_view, name="profile"),
]
