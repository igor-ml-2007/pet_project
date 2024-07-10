from django.urls import path
from shop.views import *

urlpatterns = [
    path('product-list/', ProductListAPIView.as_view()),
    path('product-filter/', ProductFilterListAPIView.as_view()),
    path('<int:pk>/', ProductDetailAPIView.as_view()),
    path('order/', CreateOrderAPIView.as_view()),
    path('brand-category/', CategoryListAPIView.as_view())
]