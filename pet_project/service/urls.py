from django.urls import path
from service.views import *


urlpatterns = [
    path('about-service/', AboutServiceListAPIView.as_view()),
    path('we-repair/', WhatWeRepairListAPIView.as_view()),
    path('faults/', FaultsListAPIView.as_view()),
    path('describe-your-problem/', CreateDescriptionAPIView.as_view()),
    path('types-of-work/', TypesOfWorkListAPIView.as_view()),
    path('category/', WhatWeRepairCategoryListAPIView.as_view()),
    path('service-detail/', ServiceAPIView.as_view()),
    path('addresses/', AddressesListAPIView.as_view())
]