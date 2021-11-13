from django.urls import path
from . import apps, views
from .views import *
from django.views.decorators.csrf import csrf_exempt


app_name = 'regis'

urlpatterns = [
    # path('', RegisWelcomeView.as_view(), name='regisWelcome'),
    path('', regisWelcomeView, name='regisWelcome'),
    path('regHome/', RegRegistrationView.as_view(), name='regHome'),
    path('payHome/', RegPaymentView.as_view(), name='payHome'),
    path('regisList/', RegisViewPatient.as_view(), name='regisList'),
    path('regisCreate/', RegisCreatePatientView.as_view(), name='regisCreate'),
    path('patDetail/<slug:slug>', views.patient_detail, name='patientDetail'),
    path('regisSearch/', RegisSearchPatientView.as_view(), name='regisSearch'),
    path('patSearch/', csrf_exempt(views.patSearch), name='patSearch'),
]
'''
# path('regisDateList/<str:date_created>', DateCreatedView.as_view(), name='regisDateList'),
# type 'regisDateList/<2021-10-26>' view by date
# path('regisDateList/<str:date_created>', DateCreatedView.as_view(), name='regisDateList'),
# path('regis', RegisWelcomeView.as_view(), name='regisWelcome'),'''