from django.contrib import admin
from .models import *      # Patient, Purpose, Test

# Register your models here.
admin.site.register([UPatient,
                     XPatient,
                     UExam,
                     XExam,
                    UResult,])
# admin.site.register([RadDept, RadStaff, RadioUser])
