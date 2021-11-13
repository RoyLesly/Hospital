from django.urls import path, re_path
from apps.dash import views

app_name = 'dash'
urlpatterns = [
    # The home page
    path('', views.dash, name='dash'),
]