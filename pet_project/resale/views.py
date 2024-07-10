from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView
from .serializers import *


class ProductCategoryListAPIView(ListAPIView):
    queryset = ProductCategory.objects.filter(parent__isnull=True)
    serializer_class = ProductCategoryListSerializer


class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductsListSerializer


class ProductDetailAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductRetrieveSerializer


class AuctionCreateAPIView(CreateAPIView):
    queryset = Auction.objects.all()
    serializer_class = AuctionSerializer





