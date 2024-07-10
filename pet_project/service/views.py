from service.serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView
from service.models import *


class AboutServiceListAPIView(ListAPIView):
    queryset = AboutService.objects.all()
    serializer_class = AboutServiceSerializer


class WhatWeRepairListAPIView(ListAPIView):
    queryset = WhatWeRepair.objects.all()
    serializer_class = WhatWeRepairSerializer


class FaultsListAPIView(ListAPIView):
    queryset = Faults.objects.all()
    serializer_class = FaultsSerializer


class CreateDescriptionAPIView(CreateAPIView):
    queryset = DescribeFault.objects.all()
    serializer_class = CreateDescribeFaultSerializer


class TypesOfWorkListAPIView(ListAPIView):
    queryset = TypesOfWork.objects.all()
    serializer_class = TypesOfWorkSerializer


class WhatWeRepairCategoryListAPIView(ListAPIView):
    queryset = WhatWeRepairCategory.objects.filter(parent__isnull=True)
    serializer_class = WhatWeRepairCategoryListSerializer


class ServiceAPIView(RetrieveAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer


class AddressesListAPIView(ListAPIView):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
