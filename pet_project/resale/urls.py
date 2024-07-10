from django.urls import path
from resale.views import *


urlpatterns = [
    path('category-list/', ProductCategoryListAPIView.as_view()),
    path('product-list/', ProductListAPIView.as_view()),
    path('product-detail/', ProductDetailAPIView.as_view()),
    path('suggest-price/', AuctionCreateAPIView.as_view())
]