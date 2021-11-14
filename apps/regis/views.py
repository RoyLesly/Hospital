from django.shortcuts import render

# Create your views here.
from django.core import serializers
from django.http import JsonResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
from django.urls import reverse_lazy
from django.shortcuts import render
from apps.radio.models import XExam, XPatient
from .models import Patient, Purpose, RegisUser
from .forms import RegPatientForm, PurposeForm
from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
# from .mixins import AjaxFormMixin


# Create your views here.
'''
class RegisWelcomeView(LoginRequiredMixin, View):
    login_url = reverse_lazy('authentication:login')

    def get(self, request):
        context = {
            "title": 'Registration and Payment Department',
            "page_title": 'Welcome to "R"'
        }
        return render(request, "regis/reg/regis_welcome.html", context)
'''


def regUserList(request):
    allUser = RegisUser.objects.all().order_by('username_id')
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
def regisWelcomeView(request):
    check = regUserList(request)
    if check == True:
        context = {
            "title": 'Registration Department',
            "page_title": 'Welcome to "REGISTRATION"'
        }
        return render(request, 'regis/regis_welcome.html', context)
    else:
        print("Not Department User")
        return render(request, 'root/welcome.html')


class RegRegistrationView(LoginRequiredMixin, View):
    login_url = reverse_lazy('authentication:login')

    def get(self, request):
        context = {
            "title": 'Registration',
            'page_title': 'Registration',
            'subtitle': 'HOME PAGE',
            "short_title": 'RH'
        }
        return render(request, 'regis/reg/regR_home.html', context)


class RegPaymentView(LoginRequiredMixin, View):
    login_url = reverse_lazy('authentication:login')

    def get(self, request):
        context = {
            "title": 'Payment',
            'page_title': 'PAYMENT',
            'subtitle': 'HOME PAGE',
        }
        return render(request, 'regis/pay/regP_home.html', context)


class RegisViewPatient(LoginRequiredMixin, ListView):  # May as well use TemplateView
    login_url = reverse_lazy('authentication:login')

    # context_title_name = 'List'
    context_object_name = 'Patients'
    model = Patient
    template_name = "regis/reg/reg-list.html"
    ordering = ['-date_created']
    paginate_by = 11

    '''def get_queryset(self):
        return Patient.objects.all()[:15]'''


class RegisCreatePatientView(LoginRequiredMixin, CreateView):
    model = Patient
    model2 = Purpose
    form_class2 = RegPatientForm  # or fields =['name', ...]
    form_class = PurposeForm
    template_name = 'regis/reg/reg-create.html'
    success_url = '/regis/regisList/'

    # optional
    def get_initial(self, *args, **kwargs):
        initial = super().get_initial(**kwargs)
        initial['age'] = 'Enter Age'
        return initial


# @login_required
def patient_detail(request, slug):
    patient_detail = Patient.objects.get(slug=slug)
    xexams = XExam.objects.all()
    print(patient_detail.slug)
    context = {"patient": patient_detail,
               "xexams": xexams}
    return render(request, 'regis/reg/reg-patientDetail.html', context)


class RegisSearchPatientView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        if request.is_ajax():
            print('post method')
            search_text = request.GET['myData']
            print(search_text)
            patient = Patient.objects.all()  # .filter(first_name__icontains=search_text)
            patient_serializers = serializers.serialize('json', patient)
            result_query = patient_serializers
            return JsonResponse(result_query, safe=False)
        return JsonResponse({'message': 'Wrong Validation'}, status=200)


import json
from django.core import serializers
from apps.radio.models import *


def patSearch(request):
    if request.method == 'GET':
        print("get")

    if request.method == 'POST':
        print(b"ajax request: " + request.body)
        search_str = json.loads(request.body).get('searchText')

        patients = XExam.objects.all().filter(patient_id__date_created__istartswith=search_str) \
                   | XExam.objects.all().filter(ex_sn__istartswith=search_str) \
                   #| Exam.objects.all().filter(upatient__patient__istartswith=search_str)

        '''patients = Patient.objects.all().filter(xpatient__date_created__istartswith=search_str) \
                   | Patient.objects.all().filter(xpatient__xn__istartswith=search_str) \
                   | Patient.objects.all().filter(xpatient__date_created__istartswith=search_str)'''

        print(patients, patients.count())

        '''patients = Patient.objects.all().filter(
            first_name__istartswith=search_str) | Patient.objects.all().filter(
                sn__startswith=search_str) | Patient.objects.all().filter(
                    last_name__istartswith=search_str)'''
        # data = list(patients.values())
        if patients.exists():
            data = serializers.serialize("json", patients)
            print(data)
            print("exist")
            return JsonResponse(data, safe=False)
        else:
            data = 'No Patients Found! ...'
            return JsonResponse(data, safe=False)


class DateCreatedView(LoginRequiredMixin, ListView):
    context_object_name = 'Patients'
    model = Patient
    template_name = "regis/reg-create.html"
    paginate_by = 11

    def get_queryset(self):
        return Patient.objects.filter(date_created__icontains=self.kwargs.get('date_created'))
