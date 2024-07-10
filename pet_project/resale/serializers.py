from rest_framework import serializers
from resale.models import *
from common.serializers import MediaURLSerializer


class ProductCategoryListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = ProductCategory
        fields = ('id', 'title', 'image')
        read_only_fields = fields


class ProductsListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = Product
        fields = ('id', 'image', 'title', 'price', 'seller')
        read_only_fields = fields


class MediaLibrarySerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaLibrary
        fields = ('id', 'image')
        read_only_fields = fields


class ProductRetrieveSerializer(serializers.ModelSerializer):
    image = MediaLibrarySerializer(many=True)

    class Meta:
        model = Product
        fields = '__all__'


class AuctionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Auction
        fields = ('id', 'suggest_price')
        read_only_fields = fields







