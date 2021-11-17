from django.contrib import admin
from .models import *      # Patient, Purpose, Test

# Register your models here.
# admin.site.register(RegisUser)
admin.site.register(Patient)
admin.site.register(Purpose)
admin.site.register(Test)
