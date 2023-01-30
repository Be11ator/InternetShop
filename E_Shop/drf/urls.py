from .views import *
from django.urls import path, re_path, include
from rest_framework import routers

urlpatterns = [

    path('api/v1/products/',  ListProductsAPIView.as_view()),
    path('api/v1/products/<int:pk>/', RetrieveUpdateProdcutAPIView.as_view()),
    path('api/v1/colors/',  ListColorsAPIView.as_view()),
    path('api/v1/colors/<int:pk>/', RetrieveUpdateColorsAPIView.as_view()),
    path('api/v1/sizes/', ListSizeAPIView.as_view()),
    path('api/v1/sizes/<int:pk>/', RetrieveUpdateSizeAPIView.as_view()),
    path('api/v1/brands/', ListBrandAPIView.as_view()),
    path('api/v1/brands/<int:pk>/', RetrieveUpdateBrandAPIView.as_view()),

]