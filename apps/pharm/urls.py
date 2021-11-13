from django.urls import path
from . import apps
from .views import *

app_name = 'pharm'

urlpatterns = [
    #path('', RadioWelcomeView.as_view(), name='radioWelcome'),
    path('', pharmWelcomeView, name='radioWelcome'),
    path('pharmHome/', EchoHomeView.as_view(), name='pharmHome'),
    path('storeHome/', XrayHomeView.as_view(), name='storeHome'),
]