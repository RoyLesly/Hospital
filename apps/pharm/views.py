import django
# from django.conf import settings
# from django.contrib.auth import get_user_model
# from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy

from .models import *
from django.views import View
from django.contrib.auth.decorators import login_required
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

def pharmUserList(request):
    print("test")
    allUser = PharmUser.objects.all().order_by('username_id')
    first = allUser[0].username
    second = allUser[1].username
    last = allUser.last().username
    userList = (first, second, last)
    user = request.user
    if user in userList:
        return True
    else:
        return False


@login_required(login_url="/login/")
def pharmWelcomeView(request):
    check = pharmUserList(request)
    if check == True:
        print("logged in")
        context = {
            "title": 'Medical Radiology Department',
            "page_title": 'Welcome to "RADIOLOGY"'
        }
        return render(request, 'radio/radio_welcome.html', context)
    else:
        print("Not Department User")
        return render(request, 'root/welcome.html')


class EchoHomeView(View):

    def get(self, request):
        context = {
            "title": 'Ultrasound',
            'page_title': 'ULTRASOUND',
            'subtitle': 'HOME PAGE',
            # "short_title": 'RH'
        }
        return render(request, 'echo/echo_home.html', context)


class XrayHomeView(View):

    def get(self, request):
        context = {
            "title": 'XRAY',
            # "short_title": 'PH',
            'page_title': 'XRAY',
            'subtitle': 'HOME PAGE',
        }
        return render(request, 'xray/xray_home.html', context)
