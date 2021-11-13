from django.urls import path, include
from . import apps
from .views import Welcome

app_name = 'root'

urlpatterns = [
    path('', Welcome.as_view(), name='welcome'),
    #path('account/', include('account.urls', namespace='account')),
    #path('regis/', include('regis.urls', namespace='regis')),

]