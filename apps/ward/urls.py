from django.urls import path
from . import apps
from .views import *

app_name = 'ward'

urlpatterns = [
    #path('', RadioWelcomeView.as_view(), name='radioWelcome'),
    path('', wardWelcomeView, name='wardWelcome'),
    path('wardHome/', EchoHomeView.as_view(), name='wardHome'),
    path('ward2Home/', XrayHomeView.as_view(), name='ward2Home'),
]