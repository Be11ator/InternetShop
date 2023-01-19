from django.template.defaulttags import url
from django.urls import path, re_path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('catalog/', Catalog.as_view(), name='catalog'),

    path('catalog/search', SearchProduct.as_view(), name='search_product'),
    path('register/', RedisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('product/<slug:product_name>/', Product.as_view(), name='product'),
    path('carz/', Carz.as_view(), name='carz'),
    path('brand/<slug:brand_slug>/', ShowBrand.as_view(), name='brand'),
    path('category/<slug:cat_slug>/', ShowCategory.as_view(), name='show_category')


]