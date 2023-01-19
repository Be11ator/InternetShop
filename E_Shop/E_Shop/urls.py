"""E_Shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from E_Shop import settings
from shop.views import *
from rest_framework import routers
rout = routers.DefaultRouter()
rout.register(r'product', ProductViewSetAPI, basename='women')

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('shop.urls')),
    path('captcha/', include('captcha.urls')),
    path('cart/', include('cart.urls', namespace='cart')),
    # path('api/v1/product_info/', ProductAPI.as_view()),
    # path('api/v1/product_info/<int:pk>/', ProductAPI.as_view())
    path('api/v1/', include(rout.urls)),

]
print(rout.urls)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # Доп настройка дебага для картинок при загрузки на серв
