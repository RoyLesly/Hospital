from django.contrib import admin
from .models import *


# Register your models here.
# admin.site.register([FinanceUser, FinanceDept, FinanceStaff],)
admin.site.register([Income, Expense, Balance],)
