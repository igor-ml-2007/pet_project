from shop.serializers import *
from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveAPIView


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all().order_by('-created_at')
    serializer_class = ProductListSerializer

    #TODO: Parameter is_in_home

class ProductFilterListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductDetailSerializer


class CreateOrderAPIView(CreateAPIView):
    queryset = Order.objects.all()
    serializer_class = CreateOrderSerializer


class CategoryListAPIView(ListAPIView):
    queryset = BrandCategory.objects.filter(parent__isnull=True)
    serializer_class = BrandCategoryListSerializer