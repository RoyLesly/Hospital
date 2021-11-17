from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import FinanceUser


@login_required
def welcome_view(request):
    return render(request, 'accounts/profile.html')

def AdminList(request):
    allUser = FinanceUser.objects.all().order_by('username_id')
    user = request.user
    if user in allUser:
        return True
    else:
        return False


@login_required(login_url="/login/")
def financeWelcomeView(request):
    check = AdminList(request)
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