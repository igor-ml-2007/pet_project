from rest_framework import serializers
from shop.models import *
from common.serializers import MediaURLSerializer


class BrandCategoryListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = BrandCategory
        fields = ('id', 'title', 'image')
        read_only_fields = fields


class ProductImageSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = ProductImage
        fields = ('id', 'product', 'image')
        read_only_fields = fields


class ProductListSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    price = serializers.IntegerField()
    products = ProductImageSerializer(many=True)
    color = serializers.CharField(max_length=120)


class ProductCharacteristics(serializers.Serializer):
    id = serializers.IntegerField()
    diagonal = serializers.CharField(max_length=120)
    operational_memory = serializers.CharField(max_length=120)
    product = serializers.CharField(source='product.title')
    chip = serializers.CharField(max_length=120)
    built_in_memory = serializers.CharField(max_length=120)


class AccessoryCharacteristicsSerializer(serializers.Serializer):
    material = serializers.CharField()
    accessory = serializers.CharField(source='accessory.title')
    desc = serializers.CharField()


class AccessoryListSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()
    product = serializers.CharField(source='product.title')

    class Meta:
        model = Accessories
        fields = ('title', 'image', 'desc', 'product')
        read_only_fields = fields


class AccessoryDetailSerializer(serializers.ModelSerializer):
    image = MediaURLSerializer()

    class Meta:
        model = Accessories
        fields = ('id', 'title', 'desc', 'price')
        read_only_fields = fields


class ProductDetailSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.title')
    products = ProductImageSerializer(many=True)
    characteristics = ProductCharacteristics(many=True)
    accessories = AccessoryListSerializer(many=True)
    recommended_products = serializers.SerializerMethodField()


    class Meta:
        model = Product
        fields = ('id', 'title', 'desc', 'price', 'products',
                  'category', 'recommended_products', 'report', 'accessories',
                  'characteristics')
        read_only_fields = fields

    def get_recommended_products(self, obj):
        recommended_products = Product.objects.filter(category_id=obj.category_id).exclude(id=obj.id)[:8]
        return ProductListSerializer(recommended_products, many=True)


class OrderItemSerializer(serializers.Serializer):
    product_id = serializers.IntegerField()
    quantity = serializers.IntegerField()


class CreateOrderSerializer(serializers.ModelSerializer):
    products = serializers.ListSerializer(child=OrderItemSerializer())

    class Meta:
        model = Order
        fields = ('full_name', 'address', 'products')




