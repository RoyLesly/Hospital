from django.urls import path
from . import apps
from .views import *

app_name = 'radio'

urlpatterns = [
    #path('', RadioWelcomeView.as_view(), name='radioWelcome'),
    path('', radioWelcomeView, name='radioWelcome'),
    path('echoHome/', EchoHomeView.as_view(), name='echoHome'),
    path('xrayHome/', XrayHomeView.as_view(), name='xrayHome'),
]