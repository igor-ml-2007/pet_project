from django.urls import path
from common.views import *


urlpatterns = [
    path('config/', CommonSettingsView.as_view(), name='config')
]