from rest_framework import serializers
from service.models import *
from common.serializers import MediaURLSerializer


class AboutServiceSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = AboutService
        fields = '__all__'


class WhatWeRepairSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = WhatWeRepair
        fields = ('id', 'title', 'image')
        read_only_fields = fields


class FaultsSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = Faults
        fields = ('id', 'title', 'image')
        read_only_fields = fields


class CreateDescribeFaultSerializer(serializers.ModelSerializer):
    class Meta:
        model = DescribeFault
        fields = '__all__'


class TypesOfWorkSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = TypesOfWork
        fields = ('id', 'image', 'title', 'problems')
        read_only_fields = fields


class WhatWeRepairCategoryListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = WhatWeRepairCategory
        fields = ('id', 'title', 'image')
        read_only_fields = fields


class ServicesSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()
    category = serializers.CharField(source='category.title')

    class Meta:
        model = Services
        fields = ('id', 'title', 'image', 'category')
        read_only_fields = fields


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'




