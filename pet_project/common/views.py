from django.shortcuts import render
from rest_framework.generics import RetrieveAPIView
from common.serializers import *
from common.models import *



class CommonSettingsView(RetrieveAPIView):
    serializer_class = CommonSettingsSerializer
    queryset = CommonSettings.objects.all()

    def get_object(self):
        return CommonSettings.objects.first()

